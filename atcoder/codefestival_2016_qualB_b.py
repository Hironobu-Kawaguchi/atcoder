# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

N, A, B = map(int, input().split())
S = input()
a, b = 0, 0
ans = []
for i in range(N):
    if S[i] == 'a':
        if a+b < A+B:
            a += 1
            ans.append("Yes")
        else:
            ans.append("No")
    elif S[i] == 'b':
        if a+b < A+B and b < B:
            b += 1
            ans.append("Yes")
        else:
            ans.append("No")
    else:
        ans.append("No")
for i in range(N):
    print(ans[i])
