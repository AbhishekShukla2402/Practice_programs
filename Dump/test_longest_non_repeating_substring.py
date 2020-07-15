def longest_lol(str1):

    sub ={}
    start_index  = 0
    length = 0
    max_length = 0

    for i, letter in enumerate(str1):

        if letter in sub and sub[letter] >= start_index:
            start_index = sub[letter]+1
            length = i - sub[letter]
            #sub[letter] = i

        else:

            sub[letter] = i
            length += 1
            if length>max_length:
                max_length = length

    print(sub)
    return max_length



str1 = "abcdabcfghijkkillo"
print(longest_lol(str1))
            
