list1 = [1,2,3,4,4,4,4,3,2,3,2,1,2,2,2,2,2,1,3,4,5,6,5,4,4,4]
peak=[]
peak_index=[]
ctr=0

for i in range(len(list1)):
    if i == len(list1)-1:
        break
    elif i == 0:
        pass
    elif list1[i] > list1[i-1] and list1[i] > list1[i+1]:
        peak.append(list1[i])
        peak_index.append(i)
    elif list1[i] > list1[i-1] and list1[i] == list1[i+1]:
        while(True):
            i+=1
            ctr+=1
            if list1[i] == list1[i-1] and list1[i] < list1[i+1]:
                ctr=0
                break
            elif list1[i] == list1[i-1] and list1[i] == list1[i+1]:
                pass
            elif list1[i] == list1[i-1] and list1[i] > list1[i+1]:
                peak.append(list1[i])
                peak_index.append(i-ctr)
                ctr=0
                break


print("Displaying zero indexed peaks")
for i in range(len(peak)):
    print("Peak {} at index {}".format(peak[i], peak_index[i]))
                
        
