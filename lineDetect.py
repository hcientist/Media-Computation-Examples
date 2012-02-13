def lineDetect(filename):
  orig = makePicture(filename)
  makeBw = makePicture(filename)
  for x in range(0,getWidth(orig)-1):
    for y in range(0,getHeight(orig)-1):
      here=getPixel(makeBw,x,y)
      down=getPixel(orig,x,y+1)
      right=getPixel(orig,x+1,y)
      hereL=(getRed(here)+getGreen(here)+getBlue(here))/3
      downL=(getRed(down)+getGreen(down)+getBlue(down))/3
      rightL=(getRed(right)+getGreen(right)+getBlue(right))/3
      if abs(hereL-downL)>10 and abs(hereL-rightL)>10:
        setColor(here,black)
      if abs(hereL-downL)<=10 and abs(hereL-rightL)<=10:
        setColor(here,white)
  return makeBw
