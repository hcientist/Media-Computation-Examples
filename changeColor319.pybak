def changeColor(picture, amount, color):
  '''Problem 3.19 on p. 72 of ISBN-13: 978-0136060239 
  change the quantity of red (color==1), green(color==2), 
  or blue(color==3) in picture based on amount.'''
  
  # loop over all pixels in the picture
  for pixel in getPixels(picture):
    
    # store the current amount of red, green, and blue into a list
    pixelColor = [getRed(pixel), getGreen(pixel), getBlue(pixel)]
    
    # change the amount of color in the pixel based on amount, for the 
    # component color (r, g, or b) based on color
    pixelColor[color-1] = pixelColor[color-1]*amount
    
    # set the pixel's color to the newly computed color.
    setColor(pixel, makeColor(pixelColor[0], pixelColor[1], pixelColor[2]))
    
    # this line could be more cleany written as follows, 
    # but we haven't talked about the argument-unpacking operator yet 
    # (and we probably won't, at least not in class)
    # (http://docs.python.org/tutorial/controlflow.html#unpacking-argument-lists)
    # setColor(pixel,makeColor(*pixelColor))
    # fyi: JES does not seem to like hte last line of the file to be a comment.
    