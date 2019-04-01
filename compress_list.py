# Given an array of characters, compress it in-place.

# The length after compression must always be smaller than or equal to the original array.

# Every element of the array should be a character (not int) of length 1.

# After you are done modifying the input array in-place, return the new length of the array.
def compress(chars):
    """Compress list of characters in place"""
    insertion = 0
    #use as index where we will insert
    current = chars[0]
    #start value to compare to
    count = 1
    #count of consecutive chars
    for i in range(1,len(chars)):
        if current == chars[i]:
            #value at current is equal to the next char
            count += 1
        else:
            chars[insertion] = current
            #insert the value of current at wherever insertion left off
            insertion = insertion + 1
            #update where we are inserting
            if count > 1:
                #if there are consecutive chars
                string = str(count)
                #convert int to string

                for char in string:
                    #iterate each char in string count
                    chars[insertion] = char
                    #insert value of string count into chars
                    insertion += 1
                    #update where we are inserting
            current = chars[i]
            #update value of current
            count = 1
            #reset count to 1

    chars[insertion] = current
    #make sure to insert last value of current
    insertion = insertion + 1
    #update where to insert
    if count > 1:
        #if there are consecutive chars for last current value
        string = str(count)
        #convert int to string
        for char in string:
            #iterate each char in string count
            chars[insertion] = char 
            #insert value of string count into chars 
            insertion += 1
            #update where we are inserting
            
        chars = chars[:insertion]
        #slice list so only ends where we have inserted values 
        return chars
output = compress(["a","a","b","b","c","c","c"])
print(output)