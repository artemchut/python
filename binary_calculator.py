user_inp = input("Enter your equation: ")
user_inp_decimal = ""

num = 0

i = 0 # iterator through every character
while i < len(user_inp):
    dec_num = 0
    while num < len(user_inp) and user_inp[num].isdecimal(): # finding out whether a character is a bin number or a symbol
        num += 1

    if i != num: # if it is a number:
        bin_num = user_inp[i:num][::-1] # reverse the number
        for k in range(len(bin_num)):
            if bin_num[k] == "1":
                dec_num += 2 ** k # calculate its bin value
        user_inp_decimal += str(dec_num)
        i = num
    else:
        user_inp_decimal += user_inp[i]
        i += 1
        num += 1

print(eval(user_inp_decimal))
