import random
required_nums=["25", "50", "75", "100"]
num_set=["", "", "", "", "", ""]
target=""
userAnsw=""
userFullAnsw=""
points=0

print("In this game you get a set of 6 numbers and by using all of them and maths symbols you need to get as close as possible to a target number")
num_required=int(input("Enter the number of required numbers you want to use(1-4): "))

while num_required>4 or num_required<1:
    num_required=int(input("Enter the number of required numbers you want to use(1-4): "))

#GENERATING 2 RANDOM NUMBERS

for i in range(0,num_required):
    num_set[i]=random.choice(required_nums)
    required_nums.remove(num_set[i])

for b in range(0,6-num_required):
    num_set[num_required+b]=str(random.randint(0,9))

#GENERATING A TARGET
for k in range(0,3):
    target+=str(random.randint(0,9))
target=int(target)   

print(f"Your number set is {num_set}")
print(f"Your target is {target}")

userInp=input("Enter: ")
for i in range(0, len(userInp)):
    userAnsw+=userInp[i]

userAnsw=userAnsw.split()

for j in userAnsw:
    if j != " ":
        userFullAnsw+=j 

userFullAnsw=eval(userFullAnsw)
print(f"Your result: {userFullAnsw}")
print(f"The difference between target and your answer is: {abs(userFullAnsw-target)}")

if userFullAnsw==target:
    points=100 
elif abs(userFullAnsw-target)<5:
    points=85
elif abs(userFullAnsw-target)<10:
    points=65 
elif abs(userFullAnsw-target)<25:
    points=50 
elif abs(userFullAnsw-target)<50:
    points=35
elif abs(userFullAnsw-target)<100:
    points=20
          
print(f"You have: {points} points")      
