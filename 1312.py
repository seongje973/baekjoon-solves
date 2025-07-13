a, b, c=map(int, input().split())
a=a % b
print(a)
for i in range(c):
    a = a * 10
    result = a // b
    a = a % b
print(result)
