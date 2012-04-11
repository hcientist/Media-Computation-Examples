import random
import time
class AnimatedTurtle(Turtle):
  def __init__(self, world, x, y):
    Turtle.__init__(self, x, y, world)
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

def example():
  world = makeWorld()
  turtle1 = AnimatedTurtle(world, 100, 100)
  turtle2 = AnimatedTurtle(world, 400, 400)
  turtle3 = AnimatedTurtle(world, 300, 400)
  turtle4 = AnimatedTurtle(world, 200, 400)
  n = 1

  while n < 300:
    turtle1.run()
    turtle2.run()
    turtle3.run()
    turtle4.run()
    n = n + 1 
    time.sleep(0.2)
