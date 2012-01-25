def driver():
  p = makePicture(pickAFile())
  show(p)
  color = pickAColor()
  tintAPic(p,color)
  repaint(p)
  
def tintAPic(image, color):
  for pixel in getPixels(p):
    r,g,b = getRed(pixel), getGreen(pixel), getBlue(pixel)
    r = (r+color.getRed())/2
    g = (g+color.getGreen())/2
    b = (b+color.getBlue())/2
    pixel.setRed(r)
    pixel.setGreen(g)
    pixel.setBlue(b)