l=int(input())
r=int(input())
k=int(input())
if k==2 :
    if r>2 and l<=2 :
        print(r-2)
    elif r>2 :
        print(r-l+1)
    else:
        print(0)
elif k==3:
    if r>5 and l<=5:
        print(r//3-1)
    elif r>5:
        if l%3 == 0 :
            print(r//3-l//3+1)
        else:
            print(r//3-l//3)
    else:
        print(0)
elif k==4 :
    if r>13 and l<=10 :
        print(r//2-5)
    elif r>13 and l<=13:
        print(r//2-6)
    elif r>13:
        if l%2 == 0:
            print(r//2-l//2+1)
        else:
            print(r//2-l//2)
    elif r<14 and r>9 and l<=10:
        print(1)
    else:
        print(0)
elif k==5:
    if r>14 and l<=14:
        print(r//5-2)
    elif r>14:
        if l%5 == 0:
            print(r//5-l//5+1)
        else:
            print(r//5-l//5)
    else:
        print(0)