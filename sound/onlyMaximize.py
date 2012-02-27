def onlyMaximize(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    if value < 0:
      setSampleValue(sample, -32768)