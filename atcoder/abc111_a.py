# A - AtCoder Beginner Contest 999
# https://atcoder.jp/contests/abc111/tasks/abc111_a

n = input()
ans = ''
for x in n:
    if x == '1':
        ans += '9'
    elif x == '9':
        ans += '1'
    else:
        ans += x
print(ans)
