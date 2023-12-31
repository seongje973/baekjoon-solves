from collections import deque
import sys
def Direction(field, originlist, count):
  for i in range(len(field)):
    if field[i]==originlist[count]:
      return (1,i)
    elif i>0 and field[-i]==originlist[count]:
      return (0,i)

def jiminpick(N,M):
  want=list(map(int,sys.stdin.readline().split()))
  originwant=[]
  for i in range(M):
    originwant.append(want[i])
  want.sort()
  count=0
  order_count=0
  field=deque()
  for j in range(N-M):
    field.append(0)
  for i in want:
    field.insert(i-1,i)
  while count<M:
    if field[0]==originwant[count]:
      field.popleft()
      count+=1
      continue
    re=Direction(field,originwant,count)
    if re[0]:
      for k in range(re[1]):
        field.append(field.popleft())
    else:
      for k in range(re[1]):
        field.appendleft(field.pop())
    order_count+=re[1]
  return order_count

if __name__=="__main__":
  N,M=map(int,sys.stdin.readline().split())
  print(jiminpick(N,M))