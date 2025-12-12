word = "hello"
guesses = 0
won = False

print("* means that the letter is in the word but in a different place")

while guesses < 5 and not won:
    guess = input("Enter a 5 letter word: ")
    while len(guess) != 5:
        print("It has to be 5 letters")
        guess = input("Enter a 5 letter word: ")
    
    guesses += 1
    if guess == word:
        print("You won!!")
        won = True
        continue
    
    guessed = ["-", "-", "-", "-", "-"]
    usedLetters = []

    #checking for all the letters in the correct position first
    for i in range(len(word)):
        if guess[i] == word[i]:
            guessed[i] = word[i]
            usedLetters.append(guess[i])

    #checking all the letters that are in the word but wrong index
    for i in range(len(word)):
        if guessed[i] == "-": 
            if guess[i] in word:
                if usedLetters.count(guess[i]) < word.count(guess[i]):
                    guessed[i] = "*"
                    usedLetters.append(guess[i])

    print(''.join(guessed))

print(f"The word was: {word}")
if not won:
    print("Unfortunately all of your 5 guesses were used up")
    print("You lost")
