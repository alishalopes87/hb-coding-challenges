# iterate over string
# create comp_index that stores the length of the string - i - 1
# create variable right that is assign to value at index i 
# create index left which starts at the last item index of string
# reassign index i to value of left
# reassign comp_index to value at right
# continue until comp_index = i 

def reverse_string(string):
    """Given a string return reversed"""
    string_lst = list(string)

    length = len(string_lst) 
    for i in range(length):
        print(i)
        comp_index = length - i - 1
        print(comp_index)

        if comp_index <= i:
                break
        left = string_lst[i]
        right =  string_lst[comp_index]

        string_lst[i] = right
        string_lst[comp_index] = left
    
        string = "".join(string_lst)
        return string

        
output = reverse_string("cat")
print(output)