def lnrs(str1):

    sub = {}
    cur_sub_start = 0
    cur_len = 0
    longest = 0


    for i, letter in enumerate(str1):
        if letter in sub and sub[letter] >= cur_sub_start:
            
        ### If letter is in the dictionary, and it is within the substring index we're checking,
        ### that is, if its within the start of the substring(cur_sub_start) and the current index(sub[letter])
        ### then perform the actions below


            cur_sub_start = sub[letter]+1

            ### Since we've detected a duplicate, we reset start of index from the next letter of the duplicate
            ### Example: abcdecfg  we've come across c as a duplicate, so we set the start index of our next substring
            ### from d onwards
                        
            cur_len = i - sub[letter]

            ### Taking the example of "abcdecfg", we set the value of the length of substring from the first occurence to the
            ### duplicate, here its from the letter after "c", "d", so our substring becomes "dec" and its length is 3. So our i in
            ### this case is 5, and sub[letter], that is sub["c"], is 2, so our length become 5-2=3, which is the length of "dec"
            
            sub[letter] = i

            ### We set the value of sub["c"], which was previously 2, to 5

        else:

            sub[letter] = i
            cur_len+=1
            if cur_len > longest:
                longest = cur_len

    print(sub)

    return longest

str1 = "abcdecfg"
print(lnrs(str1))

