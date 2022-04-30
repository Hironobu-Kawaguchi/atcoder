import sys
input = sys.stdin.readline

def solve(q):
    S = input().rstrip()
    ans = []
    for i in range(len(S)):
        ans.append(S[i])
        if S[i]+S[i:] < S[i:]:
            ans.append(S[i])
    print(f"Case #{q}: {''.join(ans)}")

T = int(input())
for t in range(T):
    solve(t+1)