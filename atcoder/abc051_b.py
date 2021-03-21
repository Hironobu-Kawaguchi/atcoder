# B - Sum of Three Integers
# https://atcoder.jp/contests/abc051/tasks/abc051_b
"""
2 つの整数 K,S が与えられます。
3 つの変数 X,Y,Z があり、0≦X,Y,Z≦K を満たす整数の値を取ります。
X+Y+Z=S を満たす X,Y,Z への値の割り当ては何通りありますか。
"""
"""
k, s = (int(i) for i in input().split())
cnt = 0
for x in range(k+1):
    c = s-x
    cnt += max(min(k,c)-max(0,c-k)+1,0)
print(cnt)
"""
K, S = map(int, input().split())
cnt = 0
for x in range(min(K, S)+1):
    for y in range(min(K, S-x)+1):
        if S-x-y <= K:
            cnt += 1
print(cnt)
