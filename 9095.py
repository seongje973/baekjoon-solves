T=int(input())
n=[]
max=0
a=[]
a.append(1)
a.append(2)
a.append(4)
for i in range(T):
    n.append(int(input()))
    if n[i]>max:
        max=n[i]
for i in range(3, max):
    a.append(a[i-1] + a[i-2] + a[i-3])
for i in range(T):
    print(a[n[i]-1])
