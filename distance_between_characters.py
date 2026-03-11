# functionality of the program is to find out whether all 1's are at least x spaces away from each other
def kLengthApart(nums, space): 
        spaces = 0
        one_found = False

        if space == 0 and 1 in nums: # if spaces between each 1 is zero then it automatically becomes True
            return True
        
        for i in range(len(nums)):
            if nums[i] == 1:
                # one_found stores whether at least one 1 was found and if num of spaces between them is smaller than 'spaces':
                if spaces < space and one_found: 
                    return False
                spaces = 0
                one_found = True
            else:
                spaces += 1
        return True
print(kLengthApart([1,0,0,0,1,0,0,1], 2))
