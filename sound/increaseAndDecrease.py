def increaseAndDecrease(sound):
  length = getLength(sound)
  for index in range(0, length/2):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value*2)
  for sampleIndex in range(length/2, length):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value*0.2)

def merge():
  guzdial = makeSound(getMediaPath("guzdial.wav"))
  isSound = makeSound(getMediaPath("is.wav"))
  target = makeSound(getMediaPath("sec3silence.wav"))
  index = 0
  for source in range(0, getLength(guzdial)):
    value = getSampleValueAt(guzdial, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  # 
  for source in range(0, int(0.1*getSamplingRate(target))):
    setSampleValueAt(target, index, 0)
    index = index + 1
  for source in range(0, getLength(isSound)):
    value = getSampleValueAt(isSound, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  normalize(target)
  play(target)
  return target

def normalize(sound):
    largest = 0
    for s in getSamples(sound):        
        largest = max(largest, getSampleValue(s))    
    amplification = 32767.0 / largest

    print "Largest sample value in original sound was",  largest 
    print "Amplification multiplier is", amplification   

    for s in getSamples(sound):      
        louder =  amplification * getSampleValue(s)  
        setSampleValue(s, louder)  

def splicePreamble():
  file = getMediaPath("preamble10.wav")
  source = makeSound(file)
  target = makeSound(file)   # This will be the newly spliced sound
  targetIndex =17408       #  targetIndex starts at just after "We the" in the new sound
  for sourceIndex in range( 33414, 40052):  # Where the word "United" is in the sound
    setSampleValueAt(target, targetIndex,  getSampleValueAt(source, sourceIndex))
    targetIndex = targetIndex + 1
  for sourceIndex in range(17408, 26726):   # Where the word "People" is in the sound
    setSampleValueAt(target , targetIndex, getSampleValueAt(source, sourceIndex))
    targetIndex = targetIndex + 1
  for index in range(0, 1000):                     #Stick some quiet space after that
    setSampleValueAt(target, targetIndex, 0)
    targetIndex = targetIndex + 1
  play(target)	                                     #Let's hear and return the result
  return target
