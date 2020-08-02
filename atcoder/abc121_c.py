"""
C - Energy Drink Collector
https://atcoder.jp/contests/abc121/tasks/abc121_c
栄養ドリンクにレーティング上昇効果があると聞いた高橋くんは、M 本の栄養ドリンクを買い集めることにしました。
栄養ドリンクが売られている店は N 軒あり、i 軒目の店では 1 本 Ai 円の栄養ドリンクを Bi 本まで買うことができます。
最小で何円あれば M 本の栄養ドリンクを買い集めることができるでしょうか。
なお、与えられる入力では、十分なお金があれば M 本の栄養ドリンクを買い集められることが保証されます。
"""
"""
import numpy as np
n,m=map(int,input().split())
a=np.zeros(n)
b=np.zeros(n)
for i in range(n):
    a[i],b[i]=map(int,input().split())
x=np.argsort(a)
ans=0
i=0
while m>0:
    ans+=a[x[i]]*min(b[x[i]],m)
    m-=b[x[i]]
    i+=1
print(int(ans))
"""
import numpy as np
N, M = map(int, input().split())
AB = np.empty((N, 2), dtype=np.int64)
for n in range(N):
    AB[n, :] = list(map(int, input().split()))
AB = AB[AB[:, 0].argsort(), :]
#print(AB)
n = 0
ans = 0
while M > 0:
    if M > AB[n, 1]:
        ans += AB[n, 0] * AB[n, 1]
        M -= AB[n, 1]
    else:
        ans += AB[n, 0] * M
        M = 0
    #print(ans, n ,M)
    n += 1
print(ans)