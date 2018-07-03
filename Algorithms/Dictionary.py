#Dictionaries
#----------------------------------------------------------------
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#----------------------------------------------------------------
emailAddress = ramit['email']
print emailAddress
interests = ramit['interests'] 
print interests[0]


jasmineEmail = ramit['friends']
for info in jasmineEmail:
    print info['email']
    break

#Print Jans second interest
interests = ramit['friends'] 
print interests[1]['interests'][1]
#----------------------------------------------------------------
#Letter Summary
msg = 'this'
emptyDic = {}

for i in msg:
    if i not in emptyDic:
        emptyDic[i] = '1'
    else:
        emptyDic[i] += 1
print emptyDic
#----------------------------------------------------------------
#Word Summary
msg = 'This is a message'
emptyDc = {}
newWord = msg.split()

for i in newWord:
  if i not in emptyDc:
    emptyDc[i] = '1'
  else:
    emptyDc[i] += 1
print emptyDc
#----------------------------------------------------------------
#Take the sentence and turn it into a list of words

#DONT HARDCODE this make it into a list
sentence = 'to be or not to be'
paddedSentence = sentence + ' '
words = []
wordCount = 0
currentWord = ''

for word in paddedSentence:
  if word == ' ':
    words.append(currentWord)
    currentWord =  ''
  else:
    currentWord += word'''








