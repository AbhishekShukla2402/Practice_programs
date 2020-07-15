def no_fives(a,b):
    c=[]
    c1=[]
    c2=[]
    ctr=0
    for i in range(a,b):
        c.append(i)
    c1=c[:]
    for i in range(len(c1)):
        if c1[i]%5==0 and c1[i]%10!=0:
            tmp=c1.index(c1[i])
            c2.append(tmp)
    for i in range(len(c2)):
        for j in range(len(c1)):
            if c2[i]==c1[j]:
                del c[j]
    for i in range(len(c)):
        ctr=ctr+1
        print(c[i])
    print("Number of elements: ",ctr)
