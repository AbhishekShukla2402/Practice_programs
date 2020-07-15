str1="forgeeksskeegfor"
l1=[]
l2=[]
for i in range(len(str1)):
    for j in range(len(str1)+1):
        tmp = str1[i:j]
        rev_tmp = tmp[::-1]
        #print(rev_tmp)
        if tmp == rev_tmp:
            if len(tmp)>1 and len(tmp) < len(str1):
                l1.append(tmp)

max1=0
ls=""
for i in l1:
    if len(i)>max1:
        max1=len(i)
        ls=i
print(ls)
print(l1)
        
