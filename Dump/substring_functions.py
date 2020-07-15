def longest_nonrepeating(str1):
    map1 = {}
    index = 0
    curr_length = 0
    max_length = 0

    for i, letter in enumerate(str1):
        if letter in map1 and map1[letter] >= index:
            index = map1[letter] + 1
            curr_length = i - index
            map1[letter] = i

        else:
            print(curr_length)
            map1[letter] = i
            curr_length+=1
            if curr_length > max_length:
                max_length = curr_length
    print(map1)
    
    return max_length

str1 = "abcdaebc"
print(longest_nonrepeating(str1))

#### abcdabc
#### 
