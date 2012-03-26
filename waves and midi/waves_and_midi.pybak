def sineWave(freq ,amplitude ):
  # Get a blank sound
  mySound = makeEmptySoundBySeconds(1)
  # Set sound constant
  sr = getSamplingRate(mySound) # sampling rate
  interval = 1.0/ freq # Make sure itÕs floating point
  samplesPerCycle = interval * sr # samples per cycle
  maxCycle = 2 * pi
  for pos in range (getLength(mySound )):
    rawSample = sin((pos / samplesPerCycle) * maxCycle)
    sampleVal = int(amplitude*rawSample)
    setSampleValueAt(mySound ,pos ,sampleVal)
  return mySound

def squareWave(freq,amplitude): 
  # Get a blank sound
  square = makeEmptySoundBySeconds(1)
  # Set music constants
  samplingRate = getSamplingRate(square)
  seconds = 1 # play for 1 second
  # Build tools for this wave
  # seconds per cycle
  interval = 1.0 * seconds / freq
   # use float since interval is fl point
  samplesPerCycle = interval * samplingRate
  # we need to switch every half-cycle
  samplesPerHalfCycle = int(samplesPerCycle / 2)
  sampleVal = amplitude
  s = 1
  i = 1
  for s in range (getLength(square)):
    # if end of a half-cycle
    if (i > samplesPerHalfCycle):
      # reverse the amplitude every half-cycle
      sampleVal = sampleVal * -1
      # and reinitialize the half-cycle counter
      i = 0
    setSampleValueAt(square,s,sampleVal)
    i = i + 1
  return(square)


def song():
  playNote(60,200,127)
  playNote(62,500,127)
  playNote(64,800,127)
  playNote(60,600,127)
  for i in range(1,2):
    playNote(64,120,127)
    playNote(65,120,127)
    playNote(67,60,127)