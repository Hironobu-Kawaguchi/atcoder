# https://atcoder.jp/contests/abc243/tasks/abc243_d

N, X = map(int, input().split())
S = input()

T = []
for c in S:
    if c=='U' and len(T)>0 and (T[-1]=='L' or T[-1]=='R'):
        T.pop()
    else:
        T.append(c)

for c in T:
    if c=='U': 
        X //= 2
    elif c=='L': 
        X *= 2
    else:
        X *= 2
        X += 1
print(X)


# N, X = map(int, input().split())
# S = input()

# X = list(bin(X))
# for c in S:
#     if c=='U':
#         # X = X[:-1]
#         X.pop()
#     elif c=='L':
#         # X = X + '0'
#         X.append('0')
#     else:
#         # X = X + '1'
#         X.append('1')
# print(int(''.join(X), 2))

