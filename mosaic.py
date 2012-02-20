def mosaic(p,r):
  for x in range (0,getWidth(p),r):
    for y in range (0,getHeight(p),r):
      makeAvgPixels(p,x,y,r)
  show(p)
  
def makeAvgPixels(p,x,y,rad):
  xmax = min(x+rad,getWidth(p))
  ymax = min(y+rad,getHeight(p))
  r,g,b,pixels = 0,0,0,0
  for i in range(x,xmax):
    for j in range(y,ymax):
      pix = getPixelAt(p,i,j)
      r,g,b = r+getRed(pix), g+getGreen(pix), b+getBlue(pix)
      pixels += 1
  r,g,b = r/float(pixels), g/float(pixels), b/float(pixels)
  for i in range(x,xmax):
    for j in range(y,ymax):
      pix = getPixelAt(p,i,j)
      setColor(pix,makeColor(r,g,b))