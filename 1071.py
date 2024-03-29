def do():
    str1 = "ABABABAB"
    str2 = "ABABABABABABABABABABABAB"
    
    
    # Verify if both strings has no unmatching characters
    length = min(len(str1), len(str2))

    if str1[:length] != str2[:length]:
        return ""
    
    keyword = str1[:length]

    if str1 == str2:
        rest = ""
    else:
        rest = str2[length:] if str1[length:] == "" else str1[length:]
    
    final_keyword = keyword
    j = len(keyword)
    while j > 1:
        j-= 1
        while len(keyword) % j != 0:
            j -=1
        
        idx = j
        flag = False

        while idx < len(keyword) - j and idx+j <= len(keyword):
            if keyword[idx:idx+j] != keyword[:j]:
                flag = True
                break
            idx+=j

        if flag == True:
            continue
        final_keyword = keyword[:j]
    
   
    idx = 0
    key_length = len(final_keyword)

    if len(rest) % key_length != 0:
        return ""

    while idx + key_length <= len(rest):
        if rest[idx:idx+key_length] != final_keyword:
            return ""
        idx+=key_length

    return final_keyword

print(do())