import random

playing=True
nums=["1","2","3","4","5","6","7","8","9"]
symbols=["+","-","/","*"]
alpha=True
num_questions=0
questions_correct=0

def correct_incorrect(alpha,playing,answer,num_questions,questions_correct):
    num_questions+=1
    while alpha:
        try:
            user_answer=round(float(input("Enter the answer: ")),1)
            alpha=False
        except ValueError:
            print("Please enter just integers")
    print(user_answer)
    if user_answer==13.3:
        playing=False
        
    if answer==user_answer:
        print("You got it right!!")
        questions_correct+=1
    else:
        print("You got it wrong :(")
        print(f"The correct answer was {answer}")
    if user_answer!=13.3:
        print(f"You got {questions_correct}/{num_questions} correct")
    else:
        print(f"You got {questions_correct}/{num_questions-1} correct")
    return num_questions,questions_correct,playing

def level1(playing,nums,symbols,alpha,num_questions, questions_correct):
    while playing:
        question=random.choice(nums)+random.choice(symbols[:1])+random.choice(nums)
        print(question)
        answer=round(float(eval(question)),1)
    
        num_questions,questions_correct,playing=correct_incorrect(alpha,playing,answer,num_questions,questions_correct)
        
def level2(playing,nums,symbols,alpha,num_questions, questions_correct):
    print("When giving an answer to a / question, round to 1d.p.")
    while playing:
        question=random.choice(nums)+random.choice(symbols)+random.choice(nums)
        print(question)
        answer=round(float(eval(question)),1)
    
        num_questions,questions_correct,playing=correct_incorrect(alpha,playing,answer,num_questions,questions_correct)

def level3(playing,nums,symbols,alpha,num_questions, questions_correct):
    print("When giving an answer to a / question, round to 1d.p.")
    while playing:
        question=""
        num_length=random.randint(1,2)
        for i in range(0,num_length):
            question+=random.choice(nums)
        question+=random.choice(symbols)+random.choice(nums)
        print(question)
        answer=round(float(eval(question)),1)
    
        num_questions,questions_correct,playing=correct_incorrect(alpha,playing,answer,num_questions,questions_correct)
        
def level4(playing,nums,symbols,alpha,num_questions, questions_correct):
    print("When giving an answer to a / question, round to 1d.p.")
    while playing:
        question=""
        num_length=random.randint(1,2)
        for i in range(0,num_length):
            question+=random.choice(nums)
        question+=random.choice(symbols)
        num_length=random.randint(1,2)
        for i in range(0,num_length):
            question+=random.choice(nums)
        print(question)
        answer=round(float(eval(question)),1)
    
        num_questions,questions_correct,playing=correct_incorrect(alpha,playing,answer,num_questions,questions_correct)
        
def level5(playing,nums,symbols,alpha,num_questions, questions_correct):
    print("When giving an answer to a / question, round to 1d.p.")
    while playing:
        question=""
        num_length=random.randint(1,2)
        for i in range(0,num_length):
            question+=random.choice(nums)
        question+=random.choice(symbols[2:])
        num_length=random.randint(1,2)
        for i in range(0,num_length):
            question+=random.choice(nums)
        print(question)
        answer=round(float(eval(question)),1)
        
        num_questions,questions_correct,playing=correct_incorrect(alpha,playing,answer,num_questions,questions_correct)
        
print("Enter 13.3 to end the game")
print("""Levels: [1]-easiest [2]-easy [3]-normal
[4]-hard [5]-demon""")
level=input("Enter level difficulty: ")

if level=="1":
    level1(playing,nums,symbols,alpha,num_questions,questions_correct)
elif level=="2":
    level2(playing,nums,symbols,alpha,num_questions,questions_correct)
elif level=="3":
    level3(playing,nums,symbols,alpha,num_questions,questions_correct)
elif level=="4":
    level4(playing,nums,symbols,alpha,num_questions,questions_correct)
elif level=="5":
    level5(playing,nums,symbols,alpha,num_questions,questions_correct)
else:
    print("You typed something wrong, try again")
    
        
    