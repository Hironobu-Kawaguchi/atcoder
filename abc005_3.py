# C - おいしいたこ焼きの売り方
# https://atcoder.jp/contests/abc005/tasks/abc005_3

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 各たこ焼きが作られてから経過した時間
takoyaki = []
# 今いる客の数
kyaku = 0

# 100秒目までループ
for i in range(101):
    # 客を待たせてはいけない
    if kyaku:
        print("no")
        exit()

    for j in range(n):
        # i 秒目にたこ焼きが作られていれば takoyaki に追加
        if a[j] == i:
            takoyaki.append(0)
    for k in range(m):
        # i 秒目に客が来ていれば kyaku に加算
        if b[k] == i:
            kyaku += 1

    # 客とたこ焼きがある限り売る
    while takoyaki and kyaku:
        takoyaki.pop(0)
        kyaku -= 1

    x = 0
    while x < len(takoyaki):
        # 各たこ焼きに 1 秒加算する
        takoyaki[x] += 1
        # t 秒を超えたら捨てる
        if takoyaki[x] > t:
            takoyaki.pop(x)
        else:
            x += 1

if kyaku:
    print("no")
else:
    print("yes")