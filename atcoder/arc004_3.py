# C - 平均値太郎の憂鬱 ( The melancholy of Taro Heikinchi )
# https://atcoder.jp/contests/arc004/tasks/arc004_3

X, Y = map(int, input().split('/'))

minN = 2 * X // Y

cnt = 0
for n in [minN, minN + 1]:
    sm = n * (n+1) //2
    m = sm - n * X // Y
    if (n * X) % Y == 0 and n >= 1 and m >= 1:
        print(n, m)
        cnt += 1
if cnt == 0:
    print('Impossible')
