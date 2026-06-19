# finds the number of words that can be made up using letters from 1 row on the keyboard
def findWords(words):
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    correct_words = []

    for word in words:
        for row in rows:
            correct_letters = 0
            for letter in word:
                if letter.lower() in row:
                    correct_letters += 1
            print(correct_letters, word)
            if correct_letters == len(word):
                print("now")
                correct_words.append(word)
    return correct_words
print(findWords(["Hello","Alaska","Dad","Peace"]))
        