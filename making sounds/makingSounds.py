def playAllTheNotes():
  for currentNote in range(128):
    playNote(currentNote, 500)

def playRangeOfNotesForTime(start, end, time):
  for currentNote in range(start, end+1):
    playNote(currentNote, time)

def playTheseRangesOfNotesForTime(rangesOfNotes, time):
  for r in range(0,len(rangesOfNotes), 2):
    playRangeOfNotesForTime(rangesOfNotes[r], rangesOfNotes[r+1], time)
    
#consider how we could write it if the incoming list was a list of lists
#each element in the input being a list of 2 items, the start and the end
def playTheseRangesOfNotesForTimes(rangesOfNotes, time):
  for startEnd in rangesOfNotes:
    playRangeOfNotesForTime(startEnd[0], rangesOfNotes[1], time)

def addSoundInto(sound1, sound2):
  for sampleNmr in range(0, getLength(sound1)):
    sample1 = getSampleValueAt(sound1, sampleNmr)
    sample2 = getSampleValueAt(sound2, sampleNmr)
    setSampleValueAt(sound2, sampleNmr, sample1 + sample2)

def makeChord(sound1, sound2, sound3):
   for index in range(0, getLength(sound1)):
      s1Sample = getSampleValueAt(sound1, index)
      setSampleValueAt(sound1, index, s1Sample )
      if index > 10000:
         s2Sample = getSampleValueAt(sound2, index - 10000)
         setSampleValueAt(sound1, index, s1Sample + s2Sample)
      if index > 20000:
         s3Sample = getSampleValueAt(sound3, index - 20000)
         setSampleValueAt(sound1, index, s1Sample + s2Sample + s3Sample)

def echo(sndFile, delay):
  s1 = makeSound(sndFile)
  s2 = makeSound(sndFile)
  for index in range(delay, getLength(s1)):
    echo = 0.6*getSampleValueAt(s2, index-delay)
    combo = getSampleValueAt(s1, index) + echo
    setSampleValueAt(s1, index, combo)
  play(s1)
  return s1

def echoes(s1, delay, num):
  #s1 = makeSound(sndFile)
  ends1 = getLength(s1)
  ends2 = ends1 + (delay * num) 	# convert samples
  s2 = makeEmptySound(ends2)
  amp = 1.0  # make amplitude smaller for each echo
  for echoCount in range(0, num):
    amp = amp * 0.6 # amplitude 60% smaller each time
    for posns1 in range(0, ends1):
      posns2 = posns1 + (delay*echoCount)
      val1 = getSampleValueAt(s1, posns1)*amp
      val2 = getSampleValueAt(s2, posns2)
      setSampleValueAt(s2, posns2, val1 + val2)
  #play(s2)
  return s2

def double(source):
  len = getLength(source) / 2 + 1
  target = makeEmptySound(len)
  targetIndex = 0
  for sourceIndex in range(0, getLength( source), 2):
    value = getSampleValueAt( source, sourceIndex)
    setSampleValueAt( target, targetIndex, value)
    targetIndex = targetIndex + 1
  play(target)
  return target

def half(source):
  target = makeEmptySound(getLength(source) * 2)
  sourceIndex = 0
  for targetIndex in range(0, getLength( target)):
    value = getSampleValueAt( source, int(sourceIndex))
    setSampleValueAt( target, targetIndex, value)
    sourceIndex = sourceIndex + 0.5
  play(target)
  return target

def shift1(source, factor):
  target = makeEmptySound(getLength(source))
  sourceIndex = 0

  for targetIndex in range(0, getLength( target)):
    value = getSampleValueAt( source, int(sourceIndex))
    setSampleValueAt( target, targetIndex, value)
    sourceIndex = sourceIndex + factor

  play(target)
  return target

def shift2(source, factor):
  target = makeEmptySound(getLength(source))
  sourceIndex = 0

  for targetIndex in range(0, getLength( target)):
    value = getSampleValueAt( source, int(sourceIndex))
    setSampleValueAt( target, targetIndex, value)
    sourceIndex = sourceIndex + factor
    if sourceIndex > getLength(source):
      sourceIndex = 0

  play(target)
  return target

def shift3(source, factor):
  target = makeEmptySound(int(getLength(source)*factor))
  sourceIndex = 0

  for targetIndex in range(0, getLength( target)):
    value = getSampleValueAt( source, int(targetIndex/factor))
    setSampleValueAt( target, targetIndex, value)

  play(target)
  return target
