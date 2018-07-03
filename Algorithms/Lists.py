#SUM Numbers 
number = [5,5,5]
counter = 0
for i in number:
    counter+=i
    print(counter)
#------------------------------------------------------------------    
#Largest Number
numbers2 = [1,5,3,12]
def biggestNumber(list):
    largestnumber = None
    for i in list:
        if i > largestnumber:
            largestnumber = i
    return largestnumber

print(biggestNumber(numbers2))
#------------------------------------------------------------------
#Smallest Number
SmallestNumber = [0,2,4,6,7,32,-1]
def smallerNumber(list):
    smallNum = None
    for i in list:
        if i < smallNum:
            smallNum = i
    return smallNum
print(smallerNumber(SmallestNumber))
#------------------------------------------------------------------
#Even Numbers
evenNumbers = [1,2,3,4,5,6,7,8]
for i in evenNumbers:
    if i % 2 == 0:
        print(i)
#------------------------------------------------------------------
#Positive Numbers
positiveNumbers = [1,2,3,0,5]
for i in positiveNumbers:
    if i > 0:
        print(i)
#------------------------------------------------------------------
#Positive Numbers II
positiveNumbers2 = [1,2,3,4,0,-1,-4,-7-12]
newList = []
for i in positiveNumbers2:
    if i >= 0:
        newList.append(i)
        print(newList)
#------------------------------------------------------------------
#MultiplyList
multiply = [2,2]
factor = 2
for i in multiply:
    print(factor*i)
#------------------------------------------------------------------
#Multiply Vector
list1 = [2, 4, 5] 
list2 = [2, 3, 6] 
newList = []
for i in range(len(list1)): RANGE = will take the length of the array and count through each
    newList.append(list1[i] * list2[i])
print(newList)
#------------------------------------------------------------------
#Matrix Addition
'''
#1: Create the matrix's
#2: create an empty matrix
#3: Use a for loop to count the number of elements in the first list
#4: Use a for loop to count the number of elements in the second list
#5: Create a variable to add the total for the two nested lists
'''

matrixList1 = [[1, 3],[2, 4]]
matrixList2 = [[5, 2],[1, 0]]
newMatrix = [[], []]

for i in range(len(matrixList1)):
    for j in range(len(matrixList2)):
        #Add the totals for the nested arrays
        total = matrixList1[i][j] + matrixList2[i][j]
        newMatrix[i].append(total)
print(newMatrix)
#------------------------------------------------------------------
myList = [0,1,2,2,3,4,5,4,1]
newList = []

for i in myList:
    if i not in newList:
        newList.append(i)
    else:
        pass
print newList
#------------------------------------------------------------------
#Multipply Matrix
m1 = [[12,12],[12,12]]
m2 = [[5,5], [2,2]]
result2 = [[], []]

for i in range(len(m1)):
    for j in range(len(m2)):
        total2 = m1[i][j] * m2[i][j]
        result2[i].append(total2)
print(result2)
#------------------------------------------------------------------
