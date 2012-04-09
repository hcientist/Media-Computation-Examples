class SmartTurtle(Turtle):
      
  def drawSquare(self, width=100):
    for i in range (0 ,4):
      self.turnRight()
      self.forward(width)
      
      
      
      
      
      
      
      
      
      
      
      
      

def playslideshow():
  pic = makePicture(getMediaPath("barbara.jpg"))
  snd = makeSound(getMediaPath("bassoon-c4.wav"))
  show(pic)
  blockingPlay(snd)
  pic = makePicture(getMediaPath("beach.jpg"))
  snd = makeSound(getMediaPath("bassoon-e4.wav"))
  show(pic)
  blockingPlay(snd)
  pic = makePicture(getMediaPath("santa.jpg"))
  snd = makeSound(getMediaPath("bassoon-g4.wav"))
  show(pic)
  blockingPlay(snd)
  pic = makePicture(getMediaPath("jungle2.jpg"))
  snd = makeSound(getMediaPath("bassoon-c4.wav"))
  show(pic)
  blockingPlay(snd)






class slide:
  #def __init__(self, pictureFile,soundFile):
  #  self.picture = makePicture(pictureFile)
  #  self.sound = makeSound(soundFile)

  def show(self):
    show(self.picture)
    blockingPlay(self.sound)

def playslideshow2():
  slide1 = slide(getMediaPath("barbara.jpg"), getMediaPath("bassoon-c4.wav"))
  slide2 = slide(getMediaPath("beach.jpg"),getMediaPath("bassoon-e4.wav"))
  slide3 = slide(getMediaPath("santa.jpg"),getMediaPath("bassoon-g4.wav"))
  slide4 = slide(getMediaPath("jungle2.jpg"),getMediaPath("bassoon-c4.wav"))
  map(showSlide,[slide1,slide2,slide3,slide4])
