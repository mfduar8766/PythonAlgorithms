
#Numbers 
age = raw_input('What is your age? ')
print "Your age is %s" %(str(age))

cost = 5
tip = 5.0
total = cost * tip
round(total, 2)
print total
#------------------------------------------------------------------
#TIP Calc
tipInput = raw_input('How much did you tip?')
tip = float(tipInput)

billInput = raw_input('How mucj was the bill?')
bill = float(billInput)

tipRatio = tip/bill

if tipRatio < 0.10:
    print 'Thats not cool'
elif tipRatio > 0.20: 
    print 'NICE!'
else:
    print 'AVG'
#------------------------------------------------------------------
dayOfWeek = int(raw_input('Enter a day from 0-6: '))
if dayOfWeek == 0:
    print('Monday')
elif dayOfWeek == 1:
    print('Tuesday')
elif dayOfWeek == 2:
    print('Tuesday')
elif dayOfWeek == 3:
    print('Wednesday')
elif dayOfWeek == 4:
    print('Thursday')
elif dayOfWeek == 5:
    print('Friday')
elif dayOfWeek == 6:
    print('Saturday')

print(dayOfWeek)
#------------------------------------------------------------------
#Work Day
Day = int(raw_input('Enter a day from 0-6: '))
if Day >= 4:
    print('Got to work')
else:
    print('Sleep')
#------------------------------------------------------------------
# Celsius to Fahrenheit
degreesInCelc = float(raw_input('Enter a temperature in celcius:'))
celctoFaran = (degreesInCelc*1.8) + 32
print(celctoFaran)
#------------------------------------------------------------------
#Tip Calc 2
billInput = raw_input('What was the bill?')
bill = float(billInput)
serviceInput = raw_input('How was the service?')

tipPercent = 0

if serviceInput == 'good':
    tipPercent = 0.2
elif serviceInput == 'fair':
    tipPercent = 0.15
elif serviceInput == 'bad':
    tipPercent = 0.1

tipAmount = bill * tipPercent
total = bill + tipAmount
print total

#------------------------------------------------------------------
name = ('john', 'lee', 'smith')
print(name[0:4]) #The : is the range
print(name[-1:]) #THe number  and : returns just that number
#------------------------------------------------------------------
#LISTS ARRAYS
name = ['john', 'lee', 'smith']

names = ('john', 'lee', 'smith')
list(names) # Converts to an array

name.append('Abby')
print(name)
#------------------------------------------------------------------------
#LOOPS
todaySeats = ['xavier', 'bob', 'jimmy']
yesterdaySeats = ['xavier', 'jimmy', 'bob']
currentRow = 0

#Is the person in this seat different from yesterday?
while currentRow < lrn(todaySeats):
    if todaySeats[currentRow] == yesterdaySeats[currentRow]:
        print('MOVE')
    currentRow += 1
#------------------------------------------------------------------
#Print a number from 1 to 10
oneToTen = range(1,11)
for num in oneToTen:
    print(num)
#------------------------------------------------------------------
#N to M
startOn =  int(raw_input('Pick a number to start at: ')) 
endingNumber = int(raw_input('Pick a number to end on:')) 

for num in range(startOn, endingNumber):
    print(num)
#------------------------------------------------------------------
#Odd Numbers  
numbers = range(1,11)
for n in numbers:
    if n % 2 == 0:
        print(n)
#------------------------------------------------------------------
#How many coins?
coinsQuestion('Do you want more coins?')
coins = 0

while True:
    print('You have these many coins %s') %(coins)
    question = raw_input('Do you want to keep going?')
    if question == 'y' or question == 'yes':
        coins +=1
    else:
        print('Bye')
        break
#------------------------------------------------------------------
#Print Square
number = 5
for i in range(number):
    print('*' * number)
#---------------------------------------------------------------
Square II
sizeOfSquare = int(raw_input('How big is the square?'))
for i in range(sizeOfSquare):
    print('*' * sizeOfSquare)

#---------------------------------------------------------------
#BOX OR put each row into a list
width = int(raw_input('What is the width?'))
height = int(raw_input('What is the height?'))

for i in range(width -5):
    print('*' * width)
    print('*' + ' ' + ' ' + ' ' +  ' ' +  '*' * (height / height))
    print('*' + ' ' + ' ' + ' ' +  ' ' +  '*' * (height / height))
    print('*' * width)
#------------------------------------------------------------------
#Triangle
number = 1
while True:
    print(" " + ' ' + ' ' + '*' * number)
    number += 2
    print(" " + ' '+ '*' * number)
    number += 2
    print(' ' + '*' * number)
    number += 2
    print('*' * number)
    break
#------------------------------------------------------------------
#Multiplications
for i in range(12):
    i+=1
    for j in range(12) :
        j+=1
        print('{} * {} = {}'.format(i, j, j*i))
#------------------------------------------------------------------
#User String Input
inputWord = raw_input('Enter something: )
print('''
#**********
  * {} *
#**********
'''.format(inputWord))
#------------------------------------------------------------------
#Triangle Number
tri = 0
for i in range(20):
    tri+= (i+1)/2
    print('*' * tri)
#------------------------------------------------------------------
#FACTOR NUMBER
num = []
input = int(raw_input('Enter a number: ')) 
for i in range(1, input+1):
    if input % i == 0:
        num.append(i)
print(num)
#------------------------------------------------------------------
#Triangle II
height = int(raw_input('Whats the height'))
for rows in range(1, height +1):
    spaces = height - rows
    stars = rows * 2 - 1
    print(spaces + stars + spaces)
#------------------------------------------------------------------
































