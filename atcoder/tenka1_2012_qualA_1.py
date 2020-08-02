# https://atcoder.jp/contests/tenka1-2012-qualA/tasks/tenka1_2012_qualA_1

n = int(input())
ans = [1]
for i in range(n):
    ans.append(sum(ans)-ans[-1])
print(sum(ans))
