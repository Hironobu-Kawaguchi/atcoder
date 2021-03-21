# https://atcoder.jp/contests/agc014/tasks/agc014_a

A, B, C = map(int, input().split())
tmpA, tmpB, tmpC = A, B, C

ans = 0
while tmpA%2 == 0 and tmpB%2 == 0 and tmpC%2 == 0:
    ans += 1
    nxtA = (tmpB + tmpC) // 2
    nxtB = (tmpA + tmpC) // 2
    nxtC = (tmpA + tmpB) // 2
    tmpA, tmpB, tmpC = nxtA, nxtB, nxtC
    if nxtA == A and nxtB == B and nxtC == C:
        ans = -1
        break

print(ans)
