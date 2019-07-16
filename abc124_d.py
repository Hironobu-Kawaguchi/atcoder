# D - Handstand
# https://atcoder.jp/contests/abc124/tasks/abc124_d

N, K = map(int, input().split())
S = input()
Nums = []
now = 1 # 今見ている数
cnt = 0 # nowがいくつ並んでいるか
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        Nums.append(cnt)
        now = 1 - now   # 0と1を切り替えるときの計算 now ^= 1
        cnt = 1
if cnt != 0:
    Nums.append(cnt)
# 1-0-1-0-1-0-1 って感じの配列が欲しい
# 1-0-1-0-1-0 みたいに0で終わっていたら適当に1つ足す
if len(Nums) % 2 == 0:
    Nums.append(0)

Add = 2 * K + 1
# 累積和を作る
# 0 1 2 3 4 5 6
#  0 1 2 3 4 5
sum = [0] * (len(Nums) + 1)
for i in range(len(Nums)):
    sum[i + 1] = sum[i] + Nums[i]
ans = 0
# 1-0-1... の1から始めるので、偶数番目だけ見る
for i in range(0, len(Nums), 2):
    # 次のleft, rightを計算する [left, right)
    left = i
    right = min(i + Add, len(Nums))
    tmp = sum[right] - sum[left]
    ans = max(tmp, ans)

print(ans)

"""
N, K = map(int, input().split())
S = input()
Nums = []
now = 1 # 今見ている数
cnt = 0 # nowがいくつ並んでいるか
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        Nums.append(cnt)
        now = 1 - now   # 0と1を切り替えるときの計算 now ^= 1
        cnt = 1
if cnt != 0:
    Nums.append(cnt)
# 1-0-1-0-1-0-1 って感じの配列が欲しい
# 1-0-1-0-1-0 みたいに0で終わっていたら適当に1つ足す
if len(Nums) % 2 == 0:
    Nums.append(0)

Add = 2 * K + 1
ans = 0
# 尺取り法 forループの外側にleft, rightを持つ
left = 0
right = 0
tmp = 0 # [left, right)のsum
# 1-0-1... の1から始めるので、偶数番目だけ見る
for i in range(0, len(Nums), 2):
    # 次のleft, rightを計算する
    Nextleft = i
    Nextright = min(i + Add, len(Nums))
    # 左端を移動する
    while Nextleft > left:
        tmp -= Nums[left]
        left += 1
    # 右端を移動する
    while Nextright > right:
        tmp += Nums[right]
        right += 1
    ans = max(tmp, ans)

print(ans)
"""

"""
N, K = map(int, input().split())
S = input()
Nums = []
now = 1 # 今見ている数
cnt = 0 # nowがいくつ並んでいるか
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        Nums.append(cnt)
        now = 1 - now   # 0と1を切り替えるときの計算 now ^= 1
        cnt = 1
if cnt != 0:
    Nums.append(cnt)
# 1-0-1-0-1-0-1 って感じの配列が欲しい
# 1-0-1-0-1-0 みたいに0で終わっていたら適当に1つ足す
if len(Nums) % 2 == 0:
    Nums.append(0)

Add = 2 * K + 1
ans = 0
# 1-0-1... の1から始めるので、偶数番目だけ見る
for i in range(0, len(Nums), 2):
    tmp = 0
    left = i
    right = min(i + Add, len(Nums))
    for j in range(left, right):
        tmp += Nums[j]
    ans = max(tmp, ans)

print(ans)
"""
