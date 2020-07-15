def pig_latin(str1):
    return ("{}{}{}".format(str1[1:len(str1)],str1[0],"ay").capitalize())

str1="Wikipedia"
print(pig_latin(str1))
