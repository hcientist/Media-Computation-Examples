# Mice and Elephants example
# Introduction to OO concepts
import random
import time

MICE = 1
ELEPHANT = 2
class Mouse(Turtle):
  def __init__(self, world, x, y):
    Turtle.__init__(self, x, y, world)
    self.type = MICE
    colors = [red, green, blue, yellow, cyan, magenta, orange, makeColor(255,100,255)]
    self.setBodyColor(random.choice(colors))
    self.setShellColor(random.choice(colors))
    
  def run(self):
    self.forward(50)
    turnAmount = int(random.random() * 45) + 1
    Amount = random.choice([-1, 1]) * turnAmount
    self.turn(Amount)
    if self.getXPos() <= 1:
      self.turn(180)
    if self.getYPos() <= 1:
      self.turn(180)
    if self.getXPos() >= 640:
      self.turn(180)
    if self.getYPos() >= 480:
      self.turn(180)

class Elephant(Turtle):
  def __init__(self, world, x, y):
    Turtle.__init__(self, x, y, world)
    self.world = world     # keep a reference to the world to use it below
    self.type = ELEPHANT
    self.setBodyColor(makeColor(59,59,59))
    self.setShellColor(makeColor(70,70,70))
  
  # elephants only run when a mouse is nearby
  # move "me" (self) if other mice are near
  def run(self):
    for mouse in getTurtleList(self.world): # use world her
      if mouse.type == MICE:
        dist = self.getDistance(mouse.getXPos(), mouse.getYPos())
        if dist < 100:
          self.turnToFace(mouse.getXPos(), mouse.getYPos())
          direction = 180 + int(random.random()*35)
          self.turn(direction)
          self.forward(25)

def example():
  world = makeWorld()
  mouse1 = Mouse(world, 100, 100)
  mouse2 = Mouse(world, 400, 400)
  mouse3 = Mouse(world, 300, 400)
  mouse4 = Mouse(world, 200, 400)
  elephant1 = Elephant(world, 300, 300)
  elephant2 = Elephant(world, 200, 100)
  n = 1

  while n < 300:
    mouse1.run()
    mouse2.run()
    mouse3.run()
    mouse4.run()
    elephant1.run()
    elephant2.run()
    n = n + 1 
    time.sleep(0.2)

class ScaryWorld(World):
  def __init__(self):
    World.__init__(self)
  def run(self):
    for n in range(300):
      for c in getTurtleList(self):
        c.run()
      time.sleep(0.2)

def example2():
  world = ScaryWorld()
  mouse1 = Mouse(world, 100, 100)
  elephant1 = Elephant(world, 300, 300)
  world.run()

def example3(n):
  world = ScaryWorld()
  for i in range(n):
    Mouse(world, 100, 100)
  Elephant(world, 300, 300)
  Elephant(world, 300, 300)
  world.run()