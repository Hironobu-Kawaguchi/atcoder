# https://atcoder.jp/contests/tenka1-2012-qualA/tasks/tenka1_2012_qualA_2

C = input()
ans = ''
flg = True
for c in C:
    if c == ' ':
        if flg:
            ans += ','
        flg = False
    else:
        ans += c
        flg = True
print(ans)

# print(",".join(input().split()))