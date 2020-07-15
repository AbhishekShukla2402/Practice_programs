def nigger(arr):
    arr = sorted(arr)
    ctr=0
    l1=[]
    for i in range(len(arr)):
        if i != len(arr)-1 and arr[i+1] == arr[i]+1:
            ctr+=1
        else:
            ctr+=1
            l1.append(ctr)
            ctr=0
    return max(l1)
    

print(nigger([1,1,1,1]))
