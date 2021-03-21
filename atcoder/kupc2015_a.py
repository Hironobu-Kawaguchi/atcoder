# A - 東京都
# https://atcoder.jp/contests/kupc2015/tasks/kupc2015_a

t = int(input())

for i in range(t):
    s = input()
    ans = 0
    j = 0

    while j < len(s) - 4:
        # 前から5文字ずつ見ていく
        if s[j:j + 5] == "tokyo" or s[j:j + 5] == "kyoto":
            ans += 1
            # 一致すれば5文字分進める
            j += 5
        else:
            j += 1

    print(ans)
    