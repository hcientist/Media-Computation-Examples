def pumpUpTheVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value*2)

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample,value * 0.5)

def normalize(sound):
  largest = 1
  for s in getSamples(sound):        
    largest = max(largest, getSampleValue(s))    
    amplification = 32767.0 / largest

  print "Largest sample value in original sound was",  largest 
  print "Amplification multiplier is", amplification

  for s in getSamples(sound):      
    louder =  amplification * getSampleValue(s)  
    setSampleValue(s, louder)

def onlyMaximize(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    if value < 0:
      setSampleValue(sample, -32768)
