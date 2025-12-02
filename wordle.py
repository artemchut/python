word="hello"
guesses=0
won=False
guessed = ["-", "-", "-", "-", "-"]
print("* means that the letter is in the word but in a different place")
while guesses < 5 and won != True:
    guess=input("Enter a 5 letter word: ")
    while len(guess) != 5:
        print("It has to be 5 letters")
        guess=input("Enter a 5 letter word: ")
    guesses += 1
    if guess==word:
        print("You won!!")
        won=True
        continue
    for i in range(0,len(word)):
        if guess[i] == word[i]:
            guessed[i] = word[i]  
        elif guess[i] in word and guess[i]!=word[i] and guess.count(guess[i])<=word.count(guess[i]):
            guessed[i]="*"
    print("".join(guessed))
if guesses==5:        
    print("Unfortunately all of your 5 guesses were used up")  
    print("You lost")  
