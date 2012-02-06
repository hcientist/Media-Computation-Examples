def censorBarb():
  barb = makePicture(pickAFile())
  show(barb)
  for x in range(87,164):
    for y in range(103,124):
      setColor(getPixelAt(barb, x, y), black)
  repaint(barb)

def lighten(pic):
  for y in range(getHeight(pic)):
    for x in range(getWidth(pic)):
      pixel = getPixelAt(pic,x,y)
      setColor(pixel,makeLighter(getColor(pixel)))
      repaint(pic)