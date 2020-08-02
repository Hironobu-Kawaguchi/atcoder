# https://atcoder.jp/contests/abc023/tasks/abc023_b

N = int(input())
S = input()

ans = N//2
if S[ans] != 'b' or N % 2 == 0:
    ans = -1
else:
    for i in range(N-1):
        tmp = S[i] + S[i+1]
        if tmp not in ["ab", "bc", "ca"]:
            ans = -1
            break
print(ans)
