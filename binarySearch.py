numList = [10,9,8,7,6,5,4,3,2,1,0]
swapped=True
while swapped:
    swapped=False
    for i in range(0,len(numList)-1):
        if numList[i]>numList[i+1]:
            smallest=numList[i+1]
            numList[i+1]=numList[i]
            numList[i]=smallest
            swapped=True
needsFound = 7
found = False

while not found:
    if numList==[]:
        print("Number not found")
        break

    middle = len(numList) // 2
    middleValue = numList[middle]

    if needsFound == middleValue:
        print(f"The number was found in the list")
        found = True

    elif needsFound < middleValue:
        print("lower")
        numList = numList[:middle] 
        print(numList)

    else:
        print("greater")
        numList = numList[middle+1:]
        print(numList)
