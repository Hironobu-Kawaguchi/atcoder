# B - Great Ocean View
# https://atcoder.jp/contests/abc124/tasks/abc124_b

N = int(input())
H = list(map(int, input().split()))
hm = 0
cnt = 0
for i in H:
    if i >= hm:
        hm = max(hm, i)
        cnt += 1
print(cnt)