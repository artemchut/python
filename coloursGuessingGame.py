import random
colours=["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "grey", "black", "white"]
coloursSet=["", ""]
userGuess=["", ""]
userCorrect=["", ""]
tries=0
won=False

print(" [1]-Difficulty 1 \n [2]-Difficulty 2 \n [3]-Difficulty 3")
levelDiff=int(input("Enter the level difficulty: "))

#MAKING A LIST AS BIG AS A LEVEL SELECTED
while levelDiff<1 or levelDiff>3:
    print("Please select an appropriate level between 1-3")        
    levelDiff=int(input("Enter the level difficulty: "))
for level in range(0, levelDiff):
    coloursSet.append("")
    userGuess.append("")
    userCorrect.append("") 

#PICKING RANDOM COLOURS
for i in range(0, len(coloursSet)):
    randomColour=random.choice(colours)
    coloursSet[i]=randomColour
    colours.remove(randomColour)  

while won==False: 
    tries+=1 
    #CLEARS A LIST THAT HAS USER'S ANSWERS(THIS IS NEEDED IN ORDER TO BE ABLE TO CHECK IF A USER TYPED IN THE SAME COLOUR MORE THAN ONCE)
    for j in range(0, len(coloursSet)):
        userGuess[j]="" 

    for k in range(0, len(coloursSet)):
        userInp=input(f"Enter the colour number {k+1}: ").lower()
        userGuess[k]=userInp
        while userGuess.count(userInp) >=2:
            print("Use the colour only once")
            userInp=input(f"Enter the colour number {k+1}: ").lower()
            userGuess[k]=userInp

        if userGuess[k]==coloursSet[k]:
            userCorrect[k]=userGuess[k]
        elif userGuess[k] in coloursSet and userGuess[k] != coloursSet[k]:
            userCorrect[k]="Different place"
        else:
            userCorrect[k]=" "     
    print(userCorrect)  
    if userCorrect==coloursSet:
        print("You won!!")     
        print(f"It took you {tries} tries.")  
        won=True   
