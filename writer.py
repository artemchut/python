import time
sentence = "Hello! My name is Artem. I am 16 years old and I like coding. I go to NSFC and enjoy it."

for i in range(0, len(sentence)):
    print(sentence[i], end="")
    if sentence[i]=="." or sentence[i]=="," or sentence[i]=="?" or sentence[i]=="!":
        time.sleep(0.6)
    else:
        time.sleep(0.2)
