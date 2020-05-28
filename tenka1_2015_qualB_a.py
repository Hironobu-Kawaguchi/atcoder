# https://atcoder.jp/contests/tenka1-2015-qualb/tasks/tenka1_2015_qualB_a

a = [100, 100, 200]
for i in range(17):
    a.append(a[-1]+a[-2]+a[-3])
print(a[-1])
