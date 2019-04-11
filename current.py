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
def findLongestRepeatedLetters(lines):
    lines_list = lines.split(" ")
    result = []

    # max_count = lines [0]
    count = 0
    for substring in range(len(lines_list)):
        print(lines_list[substring])
        current = lines_list[substring][0]
        print(current)
        for char in range(1,len(lines_list[substring])):
            print(lines_list[substring][char])
            if current == lines_list[substring][char]:
                print("this is current:",current, "this is next",lines_list[substring][char])
                count += 1
                print(count)
            else:
                if count >= 1:
                    result.append((current,count))
                    current = lines_list[substring][char]
                    print(current)
                    count = 0
    for values in result:
        print("{} {}".format(values[0],values[1]))
    

findLongestRepeatedLetters("RIGAMAROLE CONSTRUCTIVE ASSIDUOUSLY")




