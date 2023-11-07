# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

import sys

N, D, Q = map(int, input().split())
cnt = 0
# W = list(map(int, input().split()))

def compare_items(a_index, b_index):
    if a_index == b_index:
        return 0
    global cnt
    if cnt>=Q:
        return 0
    # 1から始まるインデックスを出力
    print(f"1 1 {a_index} {b_index}", flush=True)
    cnt += 1
    result = input()
    if result == "<":
        return 1  # 大きい順にソートするため、比較の結果を逆にします
    elif result == "=":
        return 0
    elif result == ">":
        return -1  # 大きい順にソートするため、比較の結果を逆にします
    else:
        print("無効な入力です。 <, =, > のいずれかを入力してください。")
        return compare_items(a_index, b_index)

def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare_items(left[i], right[j]) <= 0:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(indices):
    
    if len(indices) <= 1:
        return indices

    mid = len(indices) // 2
    left = merge_sort(indices[:mid])
    right = merge_sort(indices[mid:])

    return merge(left, right)

indices = list(range(N))
# print(*indices, file=sys.stderr)
sorted_indices = merge_sort(indices)
# print(*sorted_indices, file=sys.stderr)

for qi in range(Q-cnt):
    nl, nr = 1, 1
    l = [1]
    r = [2]
    print(nl, nr, *l, *r, flush=True)
    res = input()

d = [-1] * N
for i in range(N):
    d[sorted_indices[i]] = i % D
print(*d, flush=True)
