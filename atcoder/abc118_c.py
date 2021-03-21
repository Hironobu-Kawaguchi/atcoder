# C - Monsters Battle Royale
# https://atcoder.jp/contests/abc118/tasks/abc118_c

N = int(input())
A = list(map(int, input().split()))

while len(A) > 1:
    minA = min(A)
    tempA = []
    tempA.append(minA)
    for a in A:
        mod = a % minA
        if mod > 0:
            tempA.append(mod)
    A = tempA

print(A[0])
