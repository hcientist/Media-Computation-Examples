# pitch/speed

def changePitch(sound, factor):
  l = getLength(sound)
  result = makeEmptySound(int(l*factor))
  for i in range(getLength(result)):
    setSampleValueAt(result, i, getSampleValueAt(sound, int(i/factor)))
  return result

# volume
def changeVolume(sound, factor):
  result = duplicateSound(sound)
  for sample in getSamples(result):
    setSampleValue(sample, getSampleValue(sample)*factor)
  return result

# noise
import random
def randomNoiseOfLength(n):
  result = makeEmptySound(n)
  for i in range(getLength(result)):
    setSampleValueAt(result, i, random.randint(-32000, 32000))
  return result
  
#splice/slip/copy