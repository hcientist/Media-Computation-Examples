def increaseRed():
  file="barbara.jpg"
  picture=makePicture(file
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p,value*1.5)
  show(picture)
  return(picture)

def increaseRed2():
  file="barbara.jpg"
  picture=makePicture(file
  for x in range(0,getWidth(picture)):
    for y in range(0,getHeight(picture)):
      px = getPixel(picture,x,y)
      value = getRed(px)
      setRed(px,value*1.5)
  show(picture)
  return(picture)

def turnRedInRange():
  brown = makeColor(57,16,8)
  file="barbara.jpg"
  picture=makePicture(file)
  for x in range(70,168):
    for y in range(56,190):
      px=getPixel(picture,x,y)
      color = getColor(px)
      if distance(color,brown)<50.0:
        redness=getRed(px)*1.5
        setRed(px,redness)
  show(picture)
  return(picture)
