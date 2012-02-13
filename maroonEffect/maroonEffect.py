def maroonEffect(image):
  '''return a maroon effected copy of image'''
  
  # see http://www.branding.unirel.vt.edu/logo-usage/official-color-usage.html
  # for information on our official colors and branding
  HOKIE_MAROON = makeColor(102,0,0)
  HOKIE_ORANGE = makeColor(255,102,0)
  return twoColorScaleImage(image, HOKIE_MAROON, HOKIE_ORANGE)
  #return twoColorScaleImage(image, HOKIE_ORANGE, HOKIE_MAROON)

def twoColorScaleImage(image, c1, c2):
  '''return a copy of image which has been 
      grayscaled, but then mapped such that 
      the black becomes c1, white:c2, and the 
      shades in between mapped to colors "between
      c1 and c2'''
  
  #first we need to know how much each color can vary
  redScale = c2.getRed()-c1.getRed()
  greenScale = c2.getGreen()-c1.getGreen()
  blueScale = c2.getBlue()-c1.getBlue()
  
  #next we need to know the differential.
  #if the input image is black on a certain pixel, we 
  #will want that pixel to be c1
  #if it's white we will want it to be c2
  #but for all the other colors we need to be able to 
  #choose a color "between" marron and orange
  dr = redScale/float(255)
  dg = greenScale/float(255)
  db = blueScale/float(255)
  
  #now, befor we get down to business, let's duplicate
  #the picture so that we don't change the input
  #(we could have put this [duplication] logic into 
  #grayScale if we wanted to)
  result = duplicatePicture(image)
  
  #it's business time!
  #grayscale the image first
  grayScale(result)
  
  #go through all the pixels in the grayScaled image
  for pixel in getPixels(result):
    #red, green, and blue are all equal now due to the call to grayScale
    lum = getRed(pixel) 
    
    #using this luminance, our differential (caluclated above), and the 
    #base color c1, we calculate the new red, green, and blue
    newRed = c1.getRed()+dr*lum
    newGreen = c1.getGreen()+dg*lum
    newBlue = c1.getBlue()+db*lum
    newColor = makeColor(newRed, newGreen, newBlue)
    setColor(pixel, newColor)
  return result

def grayScale(image):
  for pixel in getPixels(image):
    lum = (getRed(pixel) + getGreen(pixel) + getBlue(pixel))/3
    setColor(pixel,makeColor(lum,lum,lum))