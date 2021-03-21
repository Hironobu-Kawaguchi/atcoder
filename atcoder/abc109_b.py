# B - Shiritori
# https://atcoder.jp/contests/abc109/tasks/abc109_b

N = int(input())
W = []
ans = "Yes"
for i in range(N):
    text = input()
    if (i > 0 and text[0] != W[-1][-1]) or (text in W):
        ans = "No"
    W.append(text)
print(ans)
