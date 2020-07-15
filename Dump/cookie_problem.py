import random

i=0
ctr=0
n=0
#bowl1 = []
#bowl_2 = []
bowl_1 = ["v" for i in range(30)] + ["c" for i in range(10)]
bowl_2 = ["v" for i in range(20)] + ["c" for i in range(20)]
random.shuffle(bowl_1)
random.shuffle(bowl_2)
while i < 10000:
    random.shuffle(bowl_2)
    selected_bowl = random.choice([bowl_1,bowl_2])
    selected_cookie = random.choice(selected_bowl)

    if selected_cookie == "v":
        n+=1
        if selected_bowl == bowl_1:
            ctr+=1
    i+=1

print("Probability of selected bowl being 1 given that the chosen cookie was vanilla is {}".format(str((ctr/n)*100)))
