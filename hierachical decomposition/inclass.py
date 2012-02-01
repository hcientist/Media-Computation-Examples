def decreaseRed(pict):
  for p in getPixels(pict):
    value=getRed(p)
    setRed(p,value*0.5)

def increaseRed(picture):
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p,value*1.2)