import time
import random
slots=["🍒","🍎","🍓"]
balance=1000
incorrect=True
while balance>0 or bet!=0:
    print("Enter 0 to quit")
    while incorrect:
        try:
            bet=int(input("Enter your bet: "))
            incorrect=False
        except ValueError:
            print("Please enter a valid integer")
            
    if bet==0:
        break
    while bet<0:   
        print("Bet gotta be higher than 0")
        bet=int(input("Enter your bet: "))
    while bet>balance:
        print("Bet gotta be lower than ur balance")    
        bet=int(input("Enter your bet: "))
    balance-=bet

    for i in range(0,20):
        random.shuffle(slots)
        print(slots)
        time.sleep(0.2)
        print("\n")
        print("\n")
        print("\n")
        print("\n")

    for i in range(0,len(slots)):
        slots[i]=random.choice(slots)
    print(slots)   

    if slots[0]=="🍒" and slots[0]==slots[1] and slots[1]==slots[2]:
        balance+=bet*9
    elif slots[0]=="🍎" and slots[0]==slots[1] and slots[1]==slots[2]:
        balance+=bet*7
    elif slots[0]=="🍓" and slots[0]==slots[1] and slots[1]==slots[2]:
        balance+=bet*6
        
    slots=["🍒","🍎","🍓"]
    incorrect=True

    print(balance)

