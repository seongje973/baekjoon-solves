def ch_num(s1):
    sum1 = 0
    for i in range(len(s1)):
        if s1[i].isdigit():
            sum1+= int(s1[i])
    return sum1

N = int(input())
sirials = []
for i in range(N):
    s = input();
    sirials.append(s)

sirials.sort(key=lambda x: (len(x), ch_num(x), x))
for s in sirials:
    print(s)