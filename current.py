#create variable current first item in list
#create variable max start at first item
#create variable count 
#create empty list
#iterate over list starting at index 1
#compare current to list[i] if same increment count
#else current = list[i]
#result.append(current)
#result.append(count)
#current = lst[i]
#count = 1
# def compress(chars):
#     """Compress list of characters in place"""
#     insertion = 0
#     #use as index where we will insert
#     current = chars[0]
#     #start value to compare to
#     count = 1
#     #count of consecutive chars
#     for i in range(1,len(chars)):
#         if current == chars[i]:
#             #value at current is equal to the next char
#             count += 1
#         else:
#             chars[insertion] = current
#             #insert the value of current at wherever insertion left off
#             insertion = insertion + 1
#             #update where we are inserting
#             if count > 1:
#                 #if there are consecutive chars
#                 string = str(count)
#                 #convert int to string

#                 for char in string:
#                     #iterate each char in string count
#                     chars[insertion] = char
#                     #insert value of string count into chars
#                     insertion += 1
#                     #update where we are inserting
#             current = chars[i]
#             #update value of current
#             count = 1
#             #reset count to 1
def findLongestRepeatedLetters(string):
    """
    Args:
        string: str.
    Returns:
        tuple. (str, int)
    """
    current = string[0]
    count = 0
    # tup_list[i] -> (str, int count)
    tup_list = []
    # populate tup_list
    for char in string[1:]:
        if current == char:
            count += 1 
        else:
            tup_list.append((current, count))
            count = 0

    # compute max of tup_list
    #max_item = compute_max(tup_list)

    best_i = 0
    max_count = tup_list[0][1]
    for i in range(len(tup_list)):
        if tup_list[i][1] > max_count:
            max_count = tup_list[i][1]
            best_i = i
    
    return "{} {}".format(tup_list[best_i][0],tup_list[best_i][1])
    

print(findLongestRepeatedLetters("RIGAMAROLE CONSTRUCTIVE ASSIDUOUSLY"))




