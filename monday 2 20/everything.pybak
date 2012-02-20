# reflect over y=x
def reflectImage(pic):
  # this function reflects the 
  # pixels in pic about the y=x line
  
  # notice here we are swapping the dimensions
  # of the images so that the resulting image is 
  # reflected...
  targetWidth = getHeight(pic)
  targetHeight = getWidth(pic)
  
  targetPic = makeEmptyPicture(targetWidth, targetHeight)
  
  # loop over every pixel in the original image "pic"
  for y in range(getHeight(pic)):
    for x in range(getWidth(pic)):
      # and for each of these pixels, set it's color to the 
      # corresponding position in the new image "targetPic"
      originalPicPixel = getPixel(pic, x,y)
      originalPicColor = getColor(originalPicPixel)
      targetPixel = getPixel(targetPic, y,x)
      setColor(targetPixel, originalPicColor)
  return targetPic


# return

# parameter names
def decreaseBy2(origNumber):
  # return the number which is 2 less than origNumber
  return origNumber - 2
