import random
letters="abcdrfghijklmnopqrstuvwxyz"
word="hello"
scramble=[[],[],[],[],[],[]]
charsUsed=0
found=1

#   CREATES THE WORDSEARCH TABLE ITSELF   #
for j in range(0,12):
        scramble[0]+=random.choice(letters)
for i in range(1,len(scramble)):
    for k in range(3):
        scramble[i]+=random.choice(letters)
    scramble[i]+=word[charsUsed]
    scramble[i][2]=word[charsUsed]
    for k in range(8):
        scramble[i]+=random.choice(letters)
    
    charsUsed+=1
scramble[5][2]="x"
scramble[4]="xhelloxxxxxx"

for i in scramble:
    print("".join(i))
    

#  LOOKS AT EVERY ROW AND COLUMN
for i in range(0,len(scramble)):
    for k in range(0,len(scramble[i])):
        if scramble[i][k]==word[0]:
            #   LOOKS FOR THE ADJACENT LETTERS, IF OUT OF BOUND - continue
            try:
                for j in range(1,len(word)):
                    if scramble[i+j][k]==word[j]:
                        found+=1
                    # RESETS THE COUNTER IF SOME LETTERS ARE FOUND BUT NOT THE FULL WORD
                    else:
                        found=1
                        break
                    if found==len(word):
                        print(f"Start at index {i}:{k}, direction: down")
                        break
                        
                found=1
                for j in range(1,len(word)):
                    if scramble[i-j][k]==word[j]:
                        found+=1
                    # RESETS THE COUNTER IF SOME LETTERS ARE FOUND BUT NOT THE FULL WORD
                    else:
                        found=1
                        break
                    if found==len(word):
                        print(f"Start at index {i}:{k}, direction: up")
                        break
                        
                found=1
                for j in range(1,len(word)):
                    if scramble[i][k+j]==word[j]:
                        found+=1
                    # RESETS THE COUNTER IF SOME LETTERS ARE FOUND BUT NOT THE FULL WORD
                    else:
                        found=1
                        break
                    if found==len(word):
                        print(f"Start at index {i}:{k}, direction: right")
                        break
                        
                found=1
                for j in range(1,len(word)):
                    if scramble[i][k-j]==word[j]:
                        found+=1
                    # RESETS THE COUNTER IF SOME LETTERS ARE FOUND BUT NOT THE FULL WORD
                    else:
                        found=1
                        break
                    if found==len(word):
                        print(f"Start at index {i}:{k}, direction: left")
                        break
                        
            except:
                continue