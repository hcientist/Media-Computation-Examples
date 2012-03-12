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

