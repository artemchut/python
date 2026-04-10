import random

letters = "abcdefghijklmnopqrstuvwxyz"
words_to_be_found = ["hello", "eye"]

row_width = 8

letters_found = 1

puzzle = [[],[],[],[],[],[]]
# GENERATION OF THE PUZZLE
for row in range(len(puzzle)):
    for i in range(row_width):
        puzzle[row] += random.choice(letters)
            
# SHOWING THAT IT WORKS IN EVERY DIRECTION
# right
puzzle[0][2] = "h"
puzzle[0][3] = "e"
puzzle[0][4] = "l"
puzzle[0][5] = "l"
puzzle[0][6] = "o"
# left
puzzle[5][2] = "o"
puzzle[5][3] = "l"
puzzle[5][4] = "l"
puzzle[5][5] = "e"
puzzle[5][6] = "h"
# up left
puzzle[4][5] = "e"
puzzle[3][4] = "l"
puzzle[2][3] = "l"
puzzle[1][2] = "o"
# down right
puzzle[1][3] = "e"
puzzle[2][4] = "l"
puzzle[3][5] = "l"
puzzle[4][6] = "o"
# down left
puzzle[0][7] = "h"
puzzle[1][6] = "e"
puzzle[2][5] = "l"
puzzle[3][4] = "l"
puzzle[4][3] = "o"
# down
puzzle[1][7] = "e"
puzzle[2][7] = "l"
puzzle[3][7] = "l"
puzzle[4][7] = "o"
# up
puzzle[1][0] = "o"
puzzle[2][0] = "l"
puzzle[3][0] = "l"
puzzle[4][0] = "e"
# up right
puzzle[5][0] = "h"
puzzle[4][1] = "e"
puzzle[3][2] = "l"
puzzle[2][3] = "l"
puzzle[1][4] = "o"
# up right and down left
puzzle[3][1] = "y"
puzzle[2][2] = "e"

for row in puzzle:
    print(row)

for word in words_to_be_found: # checking for each word that needs to be found
    for i in range(len(puzzle)):
        for k in range(len(puzzle[i])):
            if puzzle[i][k] == word[0] or puzzle[i][k] == word[len(word)-1]:
                # RIGHT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i][k+letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: right, word: {word}")
                letters_found = 1
                
                # DOWN
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i+letters_found][k]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: down, word: {word}")
                letters_found = 1
                
                # DOWN RIGHT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i+letters_found][k+letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: down-right, word: {word}")
                letters_found = 1
                
                # DOWN LEFT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i+letters_found][k-letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: down-left, word: {word}")
                letters_found = 1

                # LEFT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i][k-letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: left, word: {word}")
                letters_found = 1
                
                # UP
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i-letters_found][k]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: up, word: {word}")
                letters_found = 1
                
                # UP LEFT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i-letters_found][k-letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: up-left, word: {word}")
                letters_found = 1
                
                # UP RIGHT
                try:
                    while letters_found < len(word) and word[letters_found] == puzzle[i-letters_found][k+letters_found]:
                        letters_found += 1
                except:pass
                if letters_found == len(word):
                    print(f"Start index: {i},{k}, direction: up-right, word: {word}")
                letters_found = 1
                
