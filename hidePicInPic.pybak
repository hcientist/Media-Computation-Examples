def hidePicInPic (wolf, sheep, wolfFidelity=3, colorChannelWidth=8):
  '''From Dr. Owen Astrahan's talk today, (the one I advertised in class)
  he showed an example of steganography. This seemed pretty simple, and
  I thought you might enjoy thinking about it.
  
  Steganography (look it up on wikipedia) is all about hiding information.
  
  This function will hide the image "wolf" in the image "sheep".
  To do this, we will use the algorithm described by Dr. Astrachan's talk.
  
  As we have seen, pictures are a bunch of pixels.
  Pixels are just a location that has a certain color.
  We represent color as the amount of red, green, and blue in the pixel in a
  range from [0,256] (inclusive, that's why i used square brackets right 
  there). We talked about how actually these 256 values are stored as 1 byte,
  or 8 bits in the computer. If you think about a decimal number such as 
  8675309, you understand that the MOST SIGNIFICANT digit is 8. The 8 is in 
  the MILLIONS place, while the LEAST SIGNIGFICANT digit is the 9, in the ONES
  place. Similarly in binary, the-left most BITS are the most significant and 
  the right-most are the least significant.
  
  The general idea of the algorithm is that if we throw away the LEAST 
  significant information stored in the color of the sheep image, we can 
  instead store there the MOST significant information in the color of the 
  wolf image. We will assume that the wolf image is no larger than the sheep
  (or else how can it hide in the sheep?!)
  
  I am putting this online because a student (not sure her/he would want their
  name here) mentioned they were interested in cryptography, and steganography
  is closely related. So here we go!'''
  
  # let's check the sizes of the 2 images first to make sure this is going to
  # work out. If the wolf is bigger than the sheep in either dimension, we will 
  # just return None to try to indicate an error.
  if getWidth(wolf) > getWidth(sheep) or getHeight(wolf) > getHeight(sheep):
    return None
  
  sheepFidelity = colorChannelWidth = wolfFidelity
  wolfInSheep = makeEmptyPicture(getWidth(sheep), getHeight(sheep))
  
  # students: we are now in an implied ELSE situation since we are no longer in 
  # the function if the condition succeeds since there's a return.
  
  # we need to look at every pixel in the wolf so that we can put it into the 
  # sheep, we would like to put the pixel from the wolf "inside" of the pixel 
  # in the sheep at the same position.
  
  # so we use the loop that gives us the pixel's location (the nested loop).
  for y in range(getHeight(sheep)):
    for x in range(getWidth(sheep)):
      resultPixel = getPixelAt(wolfInSheep, x, y)
      
      #let's get the pixel in the sheep and it's r,g,b values
      sheepPixel = getPixelAt(sheep, x,y)
      sheepRed = getRed(sheepPixel)
      sheepGreen = getGreen(sheepPixel)
      sheepBlue = getBlue(sheepPixel)
      
      if x > getWidth(wolf)-1 or y > getHeight(wolf)-1:
        setColor(resultPixel, makeColor(sheepRed, sheepGreen, sheepBlue))
      
      else:
        #let's get the pixel in the wolf and it's r,g,b values
        wolfPixel = getPixelAt(wolf, x, y)
        wolfRed = getRed(wolfPixel)
        wolfGreen = getGreen(wolfPixel)
        wolfBlue = getBlue(wolfPixel)
        
        wolfInSheepRed = getCombinedColor(wolfRed, 
                                          wolfFidelity, 
                                          sheepRed, 
                                          sheepFidelity)
        
        wolfInSheepGreen = getCombinedColor(wolfGreen, 
                                            wolfFidelity, 
                                            sheepGreen, 
                                            sheepFidelity)
        
        wolfInSheepBlue = getCombinedColor(wolfBlue, 
                                           wolfFidelity, 
                                           sheepBlue, 
                                           sheepFidelity)
        
        setColor(resultPixel, makeColor(wolfInSheepRed, 
                                        wolfInSheepGreen, 
                                        wolfInSheepBlue))
        
  return wolfInSheep

#3,5
def getCombinedColor(number, most, number2, least):
  mostBase = calculateBase(most)
  leastBase = calculateBase(least)
  return getMostSigBits(number, mostBase)/mostBase + getMostSigBits(number2, leastBase)
  
def getMostSigBits(number, base):
  return number/base*base # do not be fooled, we're working with ints, so
                          # the /base and *base do not cancel out in all cases.

def calculateBase(num):
  return 2**num