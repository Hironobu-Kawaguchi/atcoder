# https://atcoder.jp/contests/arc024/tasks/arc024_2

N = int(input())
color = []
seq = []
cnt = 1
for i in range(N):
    color.append(int(input()))
    if i:
        if color[i] == color[i-1]:
            cnt += 1
        else:
            seq.append(cnt)
            cnt = 1
else:
    if seq and color[0] == color[-1]:
        cnt += seq[0]
    seq.append(cnt)

if len(seq) == 1:   # 全て同じ
    ans = -1
else:
    ans = (max(seq) + 1) // 2
print(ans)
