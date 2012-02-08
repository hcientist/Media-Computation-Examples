def mirrorTemple():
  source = makePicture(getMediaPath("/temple.jpg"))
  mirrorPoint = 276
  for x in range(13,mirrorPoint):
    for y in range(27,97):
      print "Copying color from",x,y, " to ",mirrorPoint + mirrorPoint - 1 - x, y
      pleft = getPixel(source,x,y)
      pright = getPixel(source,mirrorPoint + mirrorPoint - 1 - x,y)
      setColor(pright,getColor(pleft))
  show(source)
  return source