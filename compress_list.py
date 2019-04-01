def compress(chars):
    insertion = 0
    current = chars[0]
    count = 1
    for i in range(1,len(chars)):
        if current == chars[i]:
            count += 1
        else:
            chars[insertion] = current
            insertion = insertion + 1
            if count > 1:
                string = str(count)

                for char in string:
                    chars[insertion] = char
                    insertion += 1
            current = chars[i]
            count = 1

    chars[insertion] = current
    insertion = insertion + 1
    if count > 1:
        string = str(count)
        for char in string:
            chars[insertion] = char  
            insertion += 1
            
        chars = chars[:insertion]
        return chars
output = compress(["a","a","b","b","c","c","c"])
print(output)