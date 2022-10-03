import math
import random
def createArray(): #creates random list of 10 ints
    myArray = [None] * 10
    for x in range(len(myArray)): #fills the list
        myArray[x] = int(random.randrange(0, 20))
    return myArray
#part1
myArray = createArray()
print(myArray)
total = 0;
for x in myArray: #finds total addition of list
    total+=x
mean = total/len(myArray)
print("The mean is:"+ str(mean))
smallest = myArray[0]
index = 0;
for x in range(len(myArray)):#finds the smallest in list
    if smallest>myArray[x]:#if current index the smallest
        smallest = myArray[x]
        index = x
print("Your smallest number is:"+str(smallest))
print("The smallest number is at index:"+str(index))

#part 2
number = int(input("Enter in a number"))
part2Array = [number%10]
number /=10
while(number>1):#runs through adding each valie to list
    part2Array.append(math.floor(number%10))
    number/=10
part2Array.reverse()
print(part2Array)

#part 3
arrayA = createArray()
arrayA.sort()
arrayB = createArray()
arrayB.sort()
arrayC = [None]
print(arrayA)
print(arrayB)
arrayAIndex = 0
arrayBIndex = 0
for x in range (len(arrayB)+len(arrayB)): #adds list b it c
    if arrayBIndex >= len(arrayB):
        arrayC.append(arrayA[arrayAIndex])
        arrayAIndex += 1
    elif arrayAIndex >= len(arrayA):
        arrayC.append(arrayB[arrayBIndex])
        arrayBIndex += 1
    elif arrayA[arrayAIndex] < arrayB[arrayBIndex]:
        arrayC.append(arrayA[arrayAIndex])
        arrayAIndex+=1
    else:
        arrayC.append(arrayB[arrayBIndex])
        arrayBIndex += 1
arrayC.pop(0)
#arrayC.sort()
print(arrayC)

