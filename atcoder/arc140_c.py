# https://atcoder.jp/contests/arc140/tasks/arc140_c

N, X = map(int, input().split())

ans = [X]
candidate = []
for i in range(1, N+1):
    if i==X: continue
    candidate.append(i)
if X*2==N:
    first_half = candidate[N//2-1:] # N:odd f=s, N:even f>s
    second_half = candidate[:N//2-1]
    second_half.reverse()
else:
    first_half = candidate[:N//2] # N:odd f=s, N:even f>s
    second_half = candidate[N//2:]
    first_half.reverse()
# print(first_half, second_half)
for i in range(N-1):
    if i%2==0:
        ans.append(first_half[i//2])
    else:
        ans.append(second_half[i//2])
print(*ans)
