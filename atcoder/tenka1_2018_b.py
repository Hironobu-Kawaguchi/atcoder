# B - Exchange
# https://tenka1-2018-beginner.contest.atcoder.jp/tasks/tenka1_2018_b

A, B , K = map(int, input().split())
for k in range(K):
    if k % 2 == 0:
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A -= A // 2
    else:
        if B % 2 == 1:
            B -= 1
        A += B // 2
        B -= B // 2
print(A, B)