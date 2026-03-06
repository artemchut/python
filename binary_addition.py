def addition():
    nums = []
    print("Enter 'stop' when you're done")
    while True:
        num = input("Enter the bin value: ")
        if num == "stop":
            break
        nums.append(num[::-1])
    
    nums.sort(key=len,reverse=True)
    
    answer = ""
    add_part_answers = []
    add_part_answers.append(nums[0])
    current_answ = ""
    pocket = 0
    for i in range(1,len(nums)):
        if len(add_part_answers[-1]) > len(nums[i]):
            nums[i] = nums[i].ljust(len(add_part_answers[-1]), "0")

        for k in range(len(nums[i])):
            if (int(add_part_answers[-1][k]) + int(nums[i][k]) + pocket) == 2:
                current_answ += "0"
                pocket = 1
            elif (int(add_part_answers[-1][k]) + int(nums[i][k]) + pocket) == 3:
                current_answ += "1"
                pocket = 1
            elif (int(add_part_answers[-1][k]) + int(nums[i][k]) + pocket) == 0:
                current_answ += "0"
            elif (int(add_part_answers[-1][k]) + int(nums[i][k]) + pocket) == 1:
                current_answ += "1"
                if pocket == 1:
                    pocket = 0
        if pocket == 1:
            current_answ += "1"
        add_part_answers.append(current_answ)
        current_answ = ""
        pocket = 0
    answer = add_part_answers[-1]
    answer = answer[::-1]
    print(f"{answer=}")

    
addition()
