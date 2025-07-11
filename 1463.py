n = int(input())

l = {1:0,2:1,3:1} 

for i in range(4,n+1):
        l[i] = l[i-1]+1
        if i%3 ==0:
            [i]=min(l[i//3] +1, l[i])
        if i%2 == 0:
            l[i]=min(l[i//2] +1,l[i])
print(l[n])