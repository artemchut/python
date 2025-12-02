mean=0

inp=input("Enter: ").split() 

for i in range(0, len(inp)):
    mean+=int(inp[i]) 
inp=sorted(inp)    

mean=mean/len(inp)   

if len(inp)%2==0:
    firstNum=inp[int(len(inp)/2)-1]
    secondNum=inp[int(len(inp)/2)]
    median=(int(inp[int(len(inp)/2)-1])+int(inp[int(len(inp)/2)]))/2
else:
    median=inp[int(len(inp)/2)]

mode=inp[-1]

range=int(inp[-1])-int(inp[0])

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {range}")

print(sorted(inp))

