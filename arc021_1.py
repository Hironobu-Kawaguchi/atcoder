# https://atcoder.jp/contests/arc021/tasks/arc021_1

A = [list(map(int, input().split())) for _ in range(4)]
# print(A)

ans = "GAMEOVER"
for i in range(3):
    for j in range(4):
        if A[i][j] == A[i+1][j]:
            ans = "CONTINUE"
            break
for i in range(4):
    for j in range(3):
        if A[i][j] == A[i][j+1]:
            ans = "CONTINUE"
            break

print(ans)
