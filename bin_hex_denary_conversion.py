def Hex_To_Bin(hex):
    hex_bin = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
               "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    hex = hex.upper().strip()

    bin = ""
 
    for i in hex:
        bin += hex_bin[i]
    return bin

def Bin_To_Hex(bin):
    hex_bin = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
               "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    # FILLING THE NUMBER IN ORDER TO BE IN GROUPS OF 4
    if len(bin) % 4 != 0:
        bin = ("0"*(4 - len(bin) % 4)) + bin
    
    hex = ""
    # CONVERTING EVERY GROUP OF 4
    for i in range(0,len(bin),4):
        for key, value in hex_bin.items():
            if value == bin[i:i+4]:
                hex += key
    return hex

def Bin_To_Den(bin):
    # REVERSING THE VALUE
    bin = bin[::-1]

    den = 0
    
    for i in range(len(bin)):
        if bin[i] == "1":
            den += 2**i
    return den

def Den_To_Bin(den):
    bin = ""
    
    # SEEING WHAT THE CLOSEST NUMBER(pow of 2) TO THE DEN VALUE IS
    n = 0
    biggest = 0
    while den > biggest:
        n += 1
        biggest = 2**n

    # SUBTRACTING THE BIGGEST VALUE POSSIBLE(pow of 2) THAT IS <= DEN NUMBER
    while n >= 0:
        if 2**n <= den:
            den -= 2**n
            bin += "1"
        else:
            bin += "0"
        n -= 1
    
    # DELETING ALL UNNECESSARY 0s AT THE START
    if bin.startswith("0"):
        bin = bin[1:]
    return bin
    
def Den_To_Hex(den):
    bin = Den_To_Bin(den)
    return Bin_To_Hex(bin)

def Hex_To_Den(hex):
    bin = Hex_To_Bin(hex)
    return Bin_To_Den(bin)


def Conversion_Type():
    option = input("Enter conversion(den to hex, bin to den, ...): ").lower().strip()
    if option == "bin to hex":
        value = input("Enter the binary value: ")
        print(Bin_To_Hex(value))
    elif option == "bin to den":
        value = input("Enter the binary value: ")
        print(Bin_To_Den(value))
    elif option == "hex to bin":
        value = input("Enter the hexadecimal value: ")
        print(Hex_To_Bin(value))
    elif option == "hex to den":
        value = input("Enter the hex value: ")
        print(Hex_To_Den(value))
    elif option == "den to bin":
        value = input("Enter the denary value: ")
        print(Den_To_Bin(value))
    elif option == "den to hex":
        value = input("Enter the den value: ")
        print(Den_To_Hex(value))
    else:
        Conversion_Type()
Conversion_Type()
