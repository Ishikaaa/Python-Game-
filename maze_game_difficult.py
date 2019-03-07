import turtle
import math
import random
from tkinter import *
from threading import Thread
a=turtle.Screen()
a.title('Difficult Level')
a.bgcolor('black')
a.setup(700,760)
a.tracer(0)
# register shapes - registration of our images
turtle.register_shape("mg_chucha_front.gif")
turtle.register_shape("mg_chucha_right.gif")
turtle.register_shape("mg_chucha_left.gif")
turtle.register_shape("mg_corn.gif")
turtle.register_shape("mg_enemy.gif")
turtle.register_shape("mg_wal.gif")

class Pen(turtle.Turtle):
  # self refers to the object that we are calling the method
  def __init__(self):
    # because Pen is child class of Turtle class . So we also have to initialise Turtle class
    turtle.Turtle.__init__(self)
    self.shape('mg_wal.gif')
    self.color('white')
    # turtle usually leaves a little trail behind because the pen is down in this case. We want pen to be up becasue we don't want to draw anything
    self.penup()
    #Speed doesn't referes to the speed of the motion. It's the animation speed. This is that which we need for out total graphice to work as a game
    #And set the speed as 0 means that speed is fastest.
    self.speed(0)

class Player(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("mg_chucha_front.gif")
    self.penup()
    self.speed(0)
    # initailly,when player starts the game then gold=0
    self.gold=0
  def destroy(self):
    # i am taking the collission treasure very away from screen
    self.goto(2000,2000)#doubt

  def go_up(self):
    move_x=player.xcor();move_y=player.ycor()+24
    if(move_x,move_y) not in walls:
      self.goto(move_x,move_y)
      self.shape("mg_chucha_front.gif")
  def go_down(self):
    move_x=player.xcor();move_y=player.ycor()-24
    if (move_x, move_y) not in walls:
      self.goto(move_x,move_y)
      self.shape("mg_chucha_front.gif")
  def go_left(self):
    move_x=player.xcor()-24;move_y=player.ycor()
    if (move_x, move_y) not in walls:
      self.goto(move_x,move_y)
      self.shape("mg_chucha_left.gif")
  def go_right(self):
    move_x=player.xcor()+24;move_y=player.ycor()
    if (move_x, move_y) not in walls:
      self.goto(move_x,move_y)
      self.shape("mg_chucha_right.gif")
  def is_collission(self,other):
    # self.xcor() is the position of x-coordinate of player and other.scor() is the position of x-coordinate of treasure.
    a=self.xcor()-other.xcor()
    b=self.ycor()-other.ycor()
    distance=math.sqrt((a**2)+(b**2))
    # if distance comes less than 5 then this means that collission occurs.
    if (distance<5):
      return True
    else:
      return False

def time_out():
    b = Tk()
    b.geometry('700x750+330+0')
    b.title("GAME OVER")
    b.configure(background='black')
    l= Label(b,text="TIME OUT!!",fg="red",font=("Algerian",50),bg='black')
    l.place(x=200,y=290)
    b.mainloop()

def win_():
    b = Tk()
    b.geometry('700x750+330+0')
    b.title("YOU WON")
    b.configure(background='black')
    l1 = Label(b, text="CONGRATULATIONS..", fg="green", font=("Algerian", 50),bg='black');l1.place(x=35, y=250)
    l= Label(b,text="YOU WON!!",fg="green",font=("Algerian",50),bg='black');l.place(x=200,y=350)
    b.mainloop()

def die_():
    b = Tk()
    b.geometry('700x750+330+0')
    b.title("GAME OVER")
    b.configure(background='black')
    l1 = Label(b, text="OOPS :(", fg="red", font=("Algerian", 50),bg='black');l1.place(x=230, y=250)
    l = Label(b, text="YOU LOSE!!", fg="red", font=("Algerian", 50),bg='black');l.place(x=185, y=350)
    b.mainloop()

class Treasure(turtle.Turtle):
  # x,y are the places where i want treasure to appear
  def __init__(self,x,y):
    turtle.Turtle.__init__(self)
    self.shape("mg_corn.gif")
    self.color("gold")
    self.penup()
    self.speed(0)
    self.gold=10
    self.goto(x,y)
  def destroy(self):
    self.goto(2100,2100)

class Enemy(turtle.Turtle):
  def __init__(self,x,y):
    turtle.Turtle.__init__(self)
    self.shape("mg_enemy.gif")
    self.color("red")
    self.penup()
    self.speed(0)
    self.goto(x,y)
    self.direction=random.choice(["up","down","left","right"])
  def move(self):
    if self.direction=="up":
      dx=0;dy=24;
    elif self.direction=="down":
      dx=0;dy=-24;
    elif self.direction=="left":
      dx=-24;dy=0;
    elif self.direction=="right":
      dx=24;dy=0;
    else:
      dx=0;dy=0;

    # when player goes close to enemy
    # here self is for enemy
    if self.is_close(player):
      if player.xcor() < self.xcor():
        self.direction="left"
      elif player.xcor() > self.xcor():
        self.direction="right"
      elif player.ycor() < self.ycor():
        self.direction="down"
      elif player.ycor() > self.ycor():
        self.direction="up"
      else:
        pass

    # calculate the spot to move
    move_x=self.xcor()+dx
    move_y=self.ycor()+dy

    if(move_x,move_y) not in walls:
      self.goto(move_x,move_y)
    else:
      self.direction=random.choice(["up","down","left","right"])

    # set timer to move next move of enemy
    #ontimer will call a function after a particuler period of time(100millisecomd-300millisecond)
    turtle.ontimer(self.move,t=random.randint(150,250))

  # self is for enemy and other is for player
  def is_close(self,other):
    a=self.xcor()-other.xcor()
    b=self.ycor()-other.ycor()
    distance=math.sqrt((a**2)+(b**2))
    if distance<75:
      return True
    else:
      return False

  def destroy(self):
    self.goto(2000,2000)

levels=[""]
treasures=[]
enemies=[]
walls=[]
flag = True

# Y represents the walls and space represents the space where the player can walk.P represents player. I will place P where i want that my player will start playing
level_1=[
    "YYYYYYYYYYYYYYYYYYYYYYYYY",
    "YP YYYYYYYE         YYYYY",
    "Y  YYYYYYY  YYYYYY  YYYYY",
    "Y      TYY  YYYYYY  YYYYY",
    "Y       YY  YYYT       YY",
    "YYYYYY  YY  YYY       TYY",
    "YYYYYY  YY  YYYYYY  YYYYY",
    "YYYYYY  YY    YYYYE YYYYY",
    "Y  YYY        YYYY TYYYYY",
    "Y  YYY  YYYYYYYYYYYYYYYYY",
    "YT        YYYYYYYYYYYYYYY",
    "Y                YYYYYYYY",
    "YYYYYYYYYYYY    EYYYYY  Y",
    "YYYYYYYYYYYYYYY  YYYYY  Y",
    "YYY TYYYYYYYYYY       E Y",
    "YYY                     Y",
    "YYY E       YYYYYYYYYYYYY",
    "YYYYYYYYYY  YYYYYYYYYYYYY",
    "YYYYYYYYYY              Y",
    "YY  TYYYYY              Y",
    "YY   YYYYYYYYYYYYY  YYYYY",
    "YY    YYYYYYYYYYYY  YYYYY",
    "YY         EYYYY        Y",
    "YYYY                   TY",
    "YYYYYYYYYYYYYYYYYYYYYYYYY"
]

levels.append(level_1)

# create level setup function
def maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      # getting character of each y,x coordinate
      co=level[y][x]
      # calculate screen x,y coordinate
      screen_x=-288+(x*24)
      screen_y=288-(y*24)
      if co=="Y":
        pen.goto(screen_x,screen_y)
        # stamp puts it on screen and leaves it there
        pen.stamp()
        walls.append((screen_x, screen_y))
      if co=="P":
        player.goto(screen_x,screen_y)
      if co=="T":
        treasures.append(Treasure(screen_x, screen_y))
      if co=="E":
        enemies.append(Enemy(screen_x,screen_y))
        # Enemy is the class name

def erasableWrite_score(gold):
    eraser = turtle.Turtle()
    eraser.hideturtle()
    eraser.color('white')
    eraser.penup()
    eraser.goto(-230, 300)
    eraser.write(gold, font=("Arial", 16, "normal"))
    eraser.speed(0)
    return eraser

pen=Pen()
player=Player()
# set up level one
maze(levels[1])# Treasure and Enemy classes are called in this

turtle.hideturtle()
turtle.penup()
turtle.color("white")
turtle.goto(-280, 300)
turtle.write("Score :", align="center", font=("Arial", 15, "bold"))

# we are saying turtle module to listen. That means turtle module is gona listen to the keyboard that something happens
turtle.listen()
# onkey(player.go_left,"Left") - when i press a certain key , i want player in this case to go left(where player is the object of Player class)
# (and go_left is the method name of Player class), Left means left arrow. So wjen i puch left arrow key on my keyboard. then it will do command according to go_left method
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

for enemy in enemies:
  enemy.move()
def clock_1(t,move):
  t.goto(200, 333)
  t.right(move)
  t.pendown()
  t.forward(30)
  t.penup()
  t.home()
def clock_():
    t.speed(0.5)
    global flag
    t.hideturtle()
    t.penup()
    t.shape('circle')
    t.color('red')
    t.shapesize(.05, .05)
    t.goto(210, 321)
    t.stamp()
    move = -90
    t.penup()
    for i in range(180):
        #turtle.ontimer(clock_1(t,move),t=0)
        clock_1(t, move)
        move += 2
    if flag:
        flag = False
        time_out()
        a.bye()
    return False

#main game loop
def hoho():
  eraseble = erasableWrite_score("0")
  while True:
    # if player collide with treasure
    if treasures:
      for treasure in treasures:
        if player.is_collission(treasure):
          # add treasure  gold to player gold
          player.gold += treasure.gold
        # destroy the treasure
          treasure.destroy()
          # removing treasure from treasures list
          treasures.remove(treasure)
          # To replavce the values of score
          eraseble.clear()
          eraseble = erasableWrite_score(player.gold)
    else:
      global flag
      flag = False
      win_()
      a.bye()
    # if enemy collide with player
    for enemy in enemies:
      if player.is_collission(enemy):
        player.destroy()
        global flag
        if flag:
          flag = False
          die_()
          a.bye()
        turtle.mainloop()
    # update screen(
    a.update()
aa=10
t = turtle.Turtle()
aa=Thread(target = hoho).start()
Thread(target = clock_).start()
turtle.mainloop()
