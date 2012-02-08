def mirrorTemple():
  source = makePicture(getMediaPath("/temple.jpg"))
  mirrorPoint = 276
  count = 0
  for x in range(13,mirrorPoint):
    for y in range(27,97):
      #print "Copying color from",x,y, " to ",mirrorPoint + mirrorPoint - 1 - x, y
      pleft = getPixel(source,x,y)
      pright = getPixel(source,mirrorPoint + mirrorPoint - 1 - x,y)
      setColor(pright,getColor(pleft))
      count = count + 1
  print count
  show(source)
  return source
  
def copyBarb(barb, canvas):
  # Set up the source and target pictures
  #barbf=getMediaPath("barbara.jpg")
  #barb = makePicture(barbf)
  #canvasf = getMediaPath("7inX95in.jpg")
  #canvas = makePicture(canvasf)
  # Now, do the actual copying
  targetX = 0
  for sourceX in range(0,getWidth(barb)):
    targetY = 0
    for sourceY in range(0,getHeight(barb)):
      color = getColor(getPixel(barb,sourceX,sourceY))
      setColor(getPixel(canvas,targetX,targetY), color)
      targetY = targetY + 1
    targetX = targetX + 1
  #show(barb)
  #show(canvas)
  return canvas

def driver():
  barbf=getMediaPath("barbara.jpg")
  barb = makePicture(barbf)
  canvasf = getMediaPath("7inX95in.jpg")
  canvas = makePicture(canvasf)
  finishedBarb = copyBarb(barb, canvas)
  show(finishedBarb)
