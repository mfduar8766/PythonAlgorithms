#Divisible by 3 or 5 up to that number and add them akk up
#Similar to odd numbers
numbers = range(1000)

def sum(list1):
    total = 0
    for i in list1:
        if i % 3 == 0 or i % 5 == 0:
            total+=i
    return total 
print(sum(numbers))
#--------------------------------------------------------------------------
#Fibinacci
nterms = 20
n1 = 0
n2 = 1
count = 0

while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth 
    count += 1
#--------------------------------------------------------------------------
#Find Largest Prime Factor
#Does this number go into it? If so does this number reduce further?
number = 600851475143
remainder = number
factor = 2
#When remainder  = 1 the problem ends

while remainder != 1:
    #Remainder is divisible by factor
    if remainder % factor == 0:
        remainder /= factor
    else:
        #Test the next number if the remainder does not go into factor
        factor+=1
print factor
#--------------------------------------------------------------------------
#Letter Summary Func
def createDictionary(msg, dict1):
    for i in msg:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    return dict1
print(createDictionary('hello', {}))
#--------------------------------------------------------------------------

