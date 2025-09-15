import random
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
specialCharacters="!#$%&()*+,-./:;<=>?@[\]^_{|}~"
for letter in range(0,5):
    randomLetter1=random.choice(letters)
    randomLetter2=random.choice(letters)
    randomLetter3=random.choice(letters)
    randomLetter4=random.choice(letters)
for number in range(0,5):
    randomNumber1=random.choice(numbers)  
    randomNumber2=random.choice(numbers) 
    randomNumber3=random.choice(numbers) 
    randomNumber4=random.choice(numbers)   
for character in specialCharacters:
    randomCharacter=random.choice(character)     

password=randomLetter1+randomLetter2+randomLetter3+randomLetter4+randomNumber1+randomNumber2+randomNumber3+randomNumber4+randomCharacter
password_list = list(password)

random.shuffle(password_list)

password = "".join(password_list)

print(password)