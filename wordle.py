word="hello"
guesses=0
correct=0
won=False
guessed = ["-", "-", "-", "-", "-"]
while guesses < 5 and won != True:
    guess=input("Enter a 5 letter word: ")
    if guess==word:
        print("You won!!")
        won=True
    while len(guess) != 5:
        print("It has to be 5 letters")
        guess=input("Enter a 5 letter word: ")
    guesses += 1
    for i in range(0,5):
        if guess[i] == word[i]:
            guessed[i] = word[i]  
            correct +=1
    print("".join(guessed))
    if correct==0:
        print("Unfortunately you got 0 correct")  
if guesses==5:        
    print("Unfortunately all of your 5 guesses were used up")  
    print("You lost")  
