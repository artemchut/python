import math
inpConv=input("Hex to bin/bin to hex/hex to den/den to hex/den to bin/bin to hex: ").lower()
binToHexValues={"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8",
                "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}

def binToHex():
        binArr=list(valueInp)
        value=""

        while len(binArr)%4 != 0:
            binArr.insert(0, "0")

        #PUTTING THEM ALL IN GROUPS OF 4
        hexGroups=[]
        for i in range(0, len(binArr), 4):
            hexGroups+=[binArr[i:i+4]]

        #TRANSLATING EACH SET INTO BINARY
        for k in range(0, len(hexGroups)):
            hexGroups[k]="".join(hexGroups[k])
            value+=binToHexValues[str(hexGroups[k])]
        return value

def denToBin():
        maxBinValue=0
        binList=[]
        denList=""
        leftValue=valueInp
        for i in range(0, valueInp):
            if maxBinValue <= valueInp:
                maxBinValue=2**i
                binList.append(str(maxBinValue))  
            else:
                continue 
        binList=list(reversed(binList))

        for k in range(0, len(binList)):
            if int(binList[k]) <= leftValue and binList[k] != "0":
                leftValue=leftValue-int(binList[k])
                denList+="1"
                binList[k]="0"
            else:
                denList+="0"      
        return denList

def hexToBin():
        hexValue=list(valueInp)
        binValue=""

        for i in hexValue:
            binValue+=str("".join([key for key, value in binToHexValues.items() if value==i])) 
        return binValue

def binToDen():
        binArrFull=0
        binArr=valueInp
        binArr=list(reversed(binArr))

        for i in range(0, len(binArr)):
            if binArr[i]=="1": 
                replacer=2**int(i)
                binArr[int(i)]=str(replacer)              
                    
        for k in range(0, len(binArr)):
            binArrFull+=int(binArr[int(k)])
        return binArrFull

def denToHex():
        denToBin()
        binArr=list(denToBin())
        value=""

        while len(binArr)%4 != 0:
            binArr.insert(0, "0")

        #PUTTING THEM ALL IN GROUPS OF 4
        hexGroups=[]
        for i in range(0, len(binArr), 4):
            hexGroups+=[binArr[i:i+4]]

        #TRANSLATING EACH SET INTO BINARY
        for k in range(0, len(hexGroups)):
            hexGroups[k]="".join(hexGroups[k])
            value+=binToHexValues[str(hexGroups[k])]
        return value

def hexToDen():
        hexToBin()
        binArrFull=0
        binArr=hexToBin()
        binArr=list(reversed(binArr))

        for i in range(0, len(binArr)):
            if binArr[i]=="1": 
                replacer=2**int(i)
                binArr[int(i)]=str(replacer)              
                    
        for k in range(0, len(binArr)):
            binArrFull+=int(binArr[int(k)])
        return binArrFull

#HEXADECIMAL TO DENARY
if inpConv=="hex to den":
    valueInp=input("Enter the hex value: ")
    
    print(hexToDen())


#DENARY TO HEXADECIMAL
elif inpConv=="den to hex":
    valueInp=int(input("Enter the denary value: "))    

    print(denToHex())


#BINARY TO HEXADECIMAL    
elif inpConv=="bin to hex":
    #FIRSTLY CONVERTING BINARY TO DENARY
    valueInp=input("Enter the binary value: ")
        
    print(binToHex())
    

#HEXADECIMAL TO BINARY
elif inpConv=="hex to bin":    
    valueInp=input("Enter the hex value: ").upper()
    
    print(hexToBin())    
       
    

#DENARY TO BINARY
elif inpConv=="den to bin":
    valueInp=int(input("Enter the denary value: "))
            
    print(denToBin())         

elif inpConv=="bin to den":
    valueInp=input("Enter the binary value: ")

    print(binToDen())

else:
    print("Try agan buddy")