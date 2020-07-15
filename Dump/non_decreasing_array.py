
a = "aaaaaaabc"
b = "aaaaaaacb"
ctr=0

if len(set(a))==1 and len(set(b))==1 and set(a)==set(b):
    print("True")

asci_a = [ord(i) for i in a]
asci_b = [ord(i) for i in b]
diff  = [abs(asci_a[i] - asci_b[i]) for i in range(len(a))]

print(diff)
for i in diff:
    if i != 0:
        ctr+=1

if ctr>2:
    print("False")
elif ctr==0:
    print("False")
else:
    print("True")
    





