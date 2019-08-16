# https://atcoder.jp/contests/abc033/tasks/abc033_c

S = list(input().split('+'))    # + で分けてリスト化
ans = 0
for s in S:
    tmp = 1
    for i in range(0, len(s), 2):   # 数字は奇数文字目(偶数文字目は*)
        if s[i] == '0':             # 0が1つでもあれば、積は0
            tmp = 0
            break
    ans += tmp
print(ans)
