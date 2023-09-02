# https://atcoder.jp/contests/intro-heuristics/submissions/29241144
import time
import random
import copy
import math

def g(d):
    return d*(d-1)//2

def f(d,q,p):
  if p==q:
    return 0
  for j in range(len(ds[q-1])):
    if ds[q-1][j]>d:
      d1=j
      break  
  
  d2=ds[p-1].index(d)
  da=ds[q-1][d1]
  db=ds[q-1][d1-1]
  dc=ds[p-1][d2+1]
  dd=ds[p-1][d2-1]
  A=slst[d-1][q-1]-slst[d-1][p-1]
  A+=clst[q-1]*(g(da-db)-g(da-d)-g(d-db))-clst[p-1]*(g(dc-dd)-g(dc-d)-g(d-dd)) 
  return A

def px(score,T):
  return (math.e)**(score/T)


t_end = time.time() + 1.8
D=int(input())
clst=list(map(int,input().split()))
slst=[list(map(int,input().split())) for _ in range(D)]
new_score=-float('inf')
tlst=[]

T0=2000
T1=600
cnt=0
T=T0

for i in range(D):
  tlst.append(random.randrange(1,27))
ds=[]
a=[0]
for i in range(26):
  ds.append(copy.copy(a))
for i in range(D):
  ds[tlst[i]-1].append(i+1)
for i in range(26):
  ds[i].append(D+1) 
while time.time() < t_end:
  cnt+=1 
  if cnt%100==0:
    t=(t_end-time.time())/1.8
    T=(T0**t)*(T1**(1-t))

  a=random.randrange(2) 
  uniform=random.uniform(0,1)
  if a==1:
    d=random.randrange(1,D+1)
    q=random.randrange(1,26+1)
    p=tlst[d-1]
    score=f(d,q,p)
    if score>0 or px(score,T)>uniform:
      tlst[d-1]=q
      ds[p-1].remove(d)
      ds[q-1].append(d)
      ds[q-1].sort()
  else:
    da=random.randrange(1,D)
    db=random.randrange(da+1,min(da+16,D+1))
    
    p=tlst[da-1]
    q=tlst[db-1]
    dsa=copy.copy(ds[p-1])
    dsb=copy.copy(ds[q-1])
    
    score=f(da,q,p)
    tlst[da-1]=q
    ds[q-1].append(da)
    ds[q-1].sort()
    ds[p-1].remove(da)
    
    score+=f(db,p,q)
    if score>0 or px(score,T)>uniform:
      tlst[db-1]=p
      ds[p-1].append(db)
      ds[p-1].sort()
      ds[q-1].remove(db)
    else:
      tlst[da-1]=p
      ds[p-1]=copy.copy(dsa)
      ds[q-1]=copy.copy(dsb)  
print(*tlst,sep='\n')