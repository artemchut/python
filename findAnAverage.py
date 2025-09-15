working=True
arr=[]
arr_sum=0
arr_average=0
while working:
    inp=input("\nEnter the number('stop' to stop)").strip().lower()
    if inp.isdigit():
        inp=int(inp)
        arr.append(inp)
    else:
        working=False
for i in arr:
    arr_sum += i
arr_average = arr_sum/len(arr)    
print(arr_average)