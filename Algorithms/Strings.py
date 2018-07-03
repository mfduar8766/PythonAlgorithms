#Copying one charecter at a time
#Can use [] to get the individual character in a string
# :2 Means start at 0 and end at index 2
#0: Means from start to end 
#------------------------------------------------------------------
name = raw_input('What is your name?: ')
message = 'Hello' + " " + name
print message

name2 = raw_input('What is your name?: ')
message2 = 'Hello' + " " + name2.upper()
print message2
print (len(name2))
print 'Your name has' + ' ' + str(len(name2)) + 'characters'

name3 = raw_input('What is your name? ')
subject = raw_input('Whats your favorite subject? ')
madlib = '%s favorite subject is %s' %(name3, subject) 
print madlib
#------------------------------------------------------------------
#Uppercase a String
uppCase = 'this'
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetLower = 'abcdefghijklmnopqrstuvwxyz'
emptyStr2 = ''
index2 = 0

for letter in uppCase:
    while True:
        if letter == alphabetLower[index2]:
            emptyStr2 += alphabetCaps[index2]
            index2 = 0
            break
        else:
             index2+=1
print emptyStr2
#------------------------------------------------------------------
#Capitalize
caps = raw_input('try')
alphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetLower = 'abcdefghijklmnopqrstuvwxyz'
empty = ''

index = 0
while True:
    if 'l' == alphabetLower[index]:
        empty += alphabetCaps[index]
        break
    else:
        index+= 1 
print empty + caps[1:]
   
#------------------------------------------------------------------
#ReverseString
mystr = raw_input('Enter something: ')
revstr = mystr[::-1]
print ("Reverse is: "+revstr)

#------------------------------------------------------------------
#LeetSpeak
paragraph = raw_input('enter')
emptyStr = ''

for char in paragraph:
    if char == 'A':
        emptyStr += "4"
    elif char == 'E':
        emptyStr += "3"
    elif char == 'G':
       emptyStr +=  '6'
    elif char == 'I':
        emptyStr += '1'
    elif char == 'O':
        emptyStr +=  '0'
    elif char == 'S':
        emptyStr +=  '5'
    elif char == 'T':
       emptyStr += '7'
print(emptyStr)
#-------------------------------------------------------------------
#Ceaser
userInput = raw_input('Enter a message')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 1
cipher = ''

for letters in userInput:
    if letters in alphabet:
        cipher+= alphabet[(alphabet.index(letters)+count) % (len(alphabet))]
print(cipher)
#-------------------------------------------------------------------
#Vowels
vowels = ('aaaaa', 'eeeee', 'iiiii', 'ooooo', 'uuuuu')
message = 'good'
newMessage = ''
#-------------------------------------------------------------------
#Dictionaries do not preserve the order of elements added
#Can replace the value but not change it
#Order in a dictionary is not preverved
letterMapping = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',

    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',

    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z',
}

msg = 'you shall not pass'
upper = ''
for char in msg:
    if char in letterMapping:
        letter = letterMapping[char]
        upper+= letter
print upper









