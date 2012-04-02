#text.py
def phonebook():
  return """
Mary:893-0234:Realtor:
Fred:897-2033:Boulder crusher:
Barney:234-2342:Professional bowler:"""

def phones():
  phones = phonebook()
  phonelist = phones.split('\n')
  newphonelist = []
  for list in phonelist:
    newphonelist.append(list.split(":"))
  return newphonelist
  
def findPhone(person):
  for people in phones():
    if people[0] == person:
      print "Phone number for",person,"is",people[1]
