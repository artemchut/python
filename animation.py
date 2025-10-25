import time
word=["he", "ll", "o!"]
space=[[]]
for i in range(0, len(space)):
    space[i]=list(" "*36)

while True:
    for j in range(12, 24):
        for i in range(0, len(word)):
            if i == 0:
                space[0][j] = word[i]
                print(f"|{"".join(space[0])}|")
            else:
                space[0][j + i] = word[i]
                print(f"|{"".join(space[0])}|")

            for i in range(0, len(space)):
                space[i] = list(" " * 36)
        time.sleep(0.2)
        print("\n")
        print("\n")

    for j in range(24,12,-1):
        for i in range(0, len(word)):
            if i == 0:
                space[0][j] = word[i]
                print(f"|{"".join(space[0])}|")
            else:
                space[0][j - i] = word[i]
                print(f"|{"".join(space[0])}|")

            for i in range(0, len(space)):
                space[i] = list(" " * 36)
        time.sleep(0.2)
        print("\n")
        print("\n")
