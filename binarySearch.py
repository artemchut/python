numList = sorted(list("0123456789"))
needsFound = "7"
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