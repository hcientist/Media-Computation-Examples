#text.py
longStr = '''A really long
string with
newlines 
in 
it.'''








def phonebook():
  return """Mary:893-0234:Realtor:
Fred:897-2033:Boulder crusher:
Barney:234-2342:Professional bowler:"""

def phones():
  phones = phonebook()
  phonelist = phones.split('\n')
  print phonelist
  newphonelist = []
  for list in phonelist:
    newphonelist.append(list.split(":"))
  return newphonelist
  
def findPhone(person):
  for people in phones():
    if people[0] == person:
      print "Phone number for",person,"is",people[1]

def formLetter(gender ,lastName ,city ,eyeColor ):
  file = open("formLetter.txt","wt")
  file.write("Dear ")
  if gender =="F":
    file.write("Ms. "+lastName+":\n")
  if gender =="M":
    file.write("Mr. "+lastName+":\n")
  file.write("I am writing to remind you of the offer ")
  file.write("that we sent to you last week. Everyone in ")
  file.write(city+" knows what an exceptional offer this is!")
  file.write("(Especially those with lovely eyes of"+eyeColor+"!)")
  file.write("We hope to hear from you soon .\n")
  file.write("Sincerely ,\n")
  file.write("I.M. Acrook , Attorney at Law")
  file.close ()