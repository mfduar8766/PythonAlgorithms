#Sum the numbers
number = [5,5,5]
def sumOfNumbers(list2):
    counter = 0
    for i in list2:
        counter+=i
    return counter 
print(sumOfNumbers(number))
#---------------------------------------------------------------------------
#LargestNumber
numbers2 = [1,5,3,12]
def biggestNumber(list1):
    largestnumber = None
    for i in list1:
        if i > largestnumber:
            largestnumber = i
    return largestnumber
print(biggestNumber(numbers2))
#---------------------------------------------------------------------------
#MultiplyList
multiply1 = [2,2]
#Add a counter to keep track of the numbers being multiplied
def multiplyList(list3, numToMultiply):
    listmultiplied = list3
    multiples = numToMultiply
    for i in listmultiplied:
        return i*multiples
print(multiplyList(multiply1, 3))
#---------------------------------------------------------------------------
#Duplicates
myListDup = [0,1,2,2,3,4,5,4,1]
def removeDuplicates(duplicateList):
    newList = []
    for items in duplicateList:
        if items not in newList:
            newList.append(items)
        else:
            pass
    return newList
print removeDuplicates(myListDup)
#---------------------------------------------------------------------------
#Multiply Vector
list1 = [2, 4, 5] 
list2 = [2, 3, 6] 

def multiplyVectors(l1, l2):
    newList = []
    for i in range(len(l1)):
        total = l1[i]*l2[i]
        newList.append(total)
    return newList
print(multiplyVectors(list1, list2))
#---------------------------------------------------------------------------
#Add Matricies
matrixList1 = [[1, 3],[2, 4]]
matrixList2 = [[5, 2],[1, 0]]

def addMatrix(m1, m2):
    newMatrix = [[],[]]
    matrix1 = m1
    matrix2 = m2

    for i in range(len(m1)):
        for j in range(len(m2)):
            total = m1[i][j] + m2[i][j]
            newMatrix[i].append(total)
    return newMatrix
print(addMatrix(matrixList1, matrixList2))
#---------------------------------------------------------------------------
