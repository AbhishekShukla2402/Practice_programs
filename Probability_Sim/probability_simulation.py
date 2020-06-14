import random
ctr=0
n=0
i=0
while i < 100000:
    a = random.randint(1,2)
    b = random.randint(1,2)

    if a==1 or b==1:
        n+=1
        if a==1:
            b=random.randint(1,2)
            if b==1:
                ctr+=1
        if b==1:
            a=random.randint(1,2)
            if a==1:
                ctr+=1
    i+=1

print(ctr)

print("Probability: {}".format(str((ctr/n)*100)))
