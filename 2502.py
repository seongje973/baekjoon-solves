D, K=map(int, input().split())
n=1
fibonacci_dp=[0,1]
for i in range(2, D):
    fibonacci_dp.append(fibonacci_dp[i-1] + fibonacci_dp[i-2])
acount=fibonacci_dp[D-2]
bcount=fibonacci_dp[D-1]
while True:
    tk=K-bcount*n
    if tk/acount==tk//acount:
        if tk//acount < n:
            print(tk//acount)
            print(n)
            break
    n += 1
        