import random
lettersTop="  A   B   C"
decorTop="-------------"
decorBottom="-------------"
won=False
spaces={"aOne": " ", "aTwo": " ", "aThree": " ", "bOne": " ", "bTwo": " ", "bThree": " ", "cOne": " ", "cTwo": " ", "cThree": " "}
newTurn=random.randint(3,4)

print("To place-type in a row first and then a column, eg: cTwo")

while won==False:
    if newTurn%2==0:

        print(lettersTop)
        
        print(f'  {spaces["aOne"]} | {spaces["bOne"]} | {spaces["cOne"]}')
        print(decorTop)
        print(f'  {spaces["aTwo"]} | {spaces["bTwo"]} | {spaces["cTwo"]}')
        print(decorBottom)
        print(f' {spaces["aThree"]} | {spaces["bThree"]} | {spaces["cThree"]}')
        print("\n X turn now")
        inp=input("Enter: ").strip()
        while inp not in spaces or spaces[inp]=="X" or spaces[inp]=="O":
            print("It has to be in range A-C, 1-3 and not used already")
            inp=input("Enter: ").strip()

        spaces[inp]="X"   

        #HORIZONTAL WIN
        if spaces["aOne"]=="X" and spaces["bOne"]=="X" and spaces["cOne"]=="X":
            print("X won!!")
            won=True
            
        elif spaces["aTwo"]=="X" and spaces["bTwo"]=="X" and spaces["cTwo"]=="X":
            print("X won!!")
            won=True
            
        elif spaces["aThree"]=="X" and spaces["bThree"]=="X" and spaces["cThree"]=="X":
            print("X won!!")  
            won=True
            

        #VERTICAL WIN
        elif spaces["aOne"]=="X" and spaces["aTwo"]=="X" and spaces["aThree"]=="X":
            print("X won!!")
            won=True
            
        elif spaces["bOne"]=="X" and spaces["bTwo"]=="X" and spaces["bThree"]=="X":
            print("X won!!")
            won=True
            
        elif spaces["cOne"]=="X" and spaces["cTwo"]=="X" and spaces["cThree"]=="X":
            print("X won!!")  
            won=True
            

        #DIAGONAL WIN
        elif spaces["aOne"]=="X" and spaces["bTwo"]=="X" and spaces["cThree"]=="X":
            print("X won!!")
            won=True
            
        elif spaces["cOne"]=="X" and spaces["bTwo"]=="X" and spaces["aThree"]=="X":
            print("X won!!")
            won=True
              

        newTurn+=1
    if newTurn%2==1:
        print(lettersTop)
        print(f'  {spaces["aOne"]} | {spaces["bOne"]} | {spaces["cOne"]}')
        print(decorTop)
        print(f' {spaces["aTwo"]} | {spaces["bTwo"]} | {spaces["cTwo"]}')
        print(decorBottom)
        print(f'  {spaces["aThree"]} | {spaces["bThree"]} | {spaces["cThree"]}')
        print("\n O turn now")

        inp=input("Enter: ").strip()

        while inp not in spaces or spaces[inp]=="1" or spaces[inp]=="X":
            print("It has to be in range A-C, 1-3 and not used already")
            inp=input("Enter: ").strip()

        spaces[inp]="O"

        #HORIZONTAL WIN
        if spaces["aOne"]=="O" and spaces["bOne"]=="O" and spaces["cOne"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        elif spaces["aTwo"]=="O" and spaces["bTwo"]=="O" and spaces["cTwo"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        elif spaces["aThree"]=="O" and spaces["bThree"]=="O" and spaces["cThree"]=="O":
            print("O won!!".center(13, " ")) 
            won=True
             
            
        #VERTICAL WIN
        elif spaces["aOne"]=="O" and spaces["aTwo"]=="O" and spaces["aThree"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        elif spaces["bOne"]=="O" and spaces["bTwo"]=="O" and spaces["bThree"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        elif spaces["cOne"]=="O" and spaces["cTwo"]=="O" and spaces["cThree"]=="O":
            print("O won!!".center(13, " ")) 
            won=True
            

        #DIAGONAL WIN
        elif spaces["aOne"]=="O" and spaces["bTwo"]=="O" and spaces["cThree"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        elif spaces["cOne"]=="O" and spaces["bTwo"]=="O" and spaces["aThree"]=="O":
            print("O won!!".center(13, " "))
            won=True
            
        newTurn+=1        

print(lettersTop)
print(f'  {spaces["aOne"]} | {spaces["bOne"]} | {spaces["cOne"]}')
print(decorTop)
print(f'  {spaces["aTwo"]} | {spaces["bTwo"]} | {spaces["cTwo"]}')
print(decorBottom)
print(f'  {spaces["aThree"]} | {spaces["bThree"]} | {spaces["cThree"]}')        
