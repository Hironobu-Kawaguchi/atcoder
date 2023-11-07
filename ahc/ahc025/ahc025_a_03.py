# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

import sys

N, D, Q = map(int, input().split())

def compare_items(a_index, b_index, cnt, max_queries):
    if a_index == b_index or cnt >= max_queries:
        return 0

    print(f"1 1 {a_index} {b_index}", flush=True)
    result = input()
    
    if result == "<":
        return 1
    elif result == "=":
        return 0
    elif result == ">":
        return -1
    else:
        print("無効な入力です。 <, =, > のいずれかを入力してください。")
        sys.exit()

def merge(left, right, cnt, max_queries):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        comparison = compare_items(left[i], right[j], cnt, max_queries)
        cnt += 1
        if comparison <= 0:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, cnt

def merge_sort(indices, cnt, max_queries):
    if len(indices) <= 1:
        return indices, cnt

    mid = len(indices) // 2
    left, cnt = merge_sort(indices[:mid], cnt, max_queries)
    right, cnt = merge_sort(indices[mid:], cnt, max_queries)

    return merge(left, right, cnt, max_queries)

cnt = 0
indices = list(range(N))
sorted_indices, cnt = merge_sort(indices, cnt, Q)

d_set = [set() for _ in range(D)]
for i in range(N):
    if (i//D)%2 == 0:
        d_set[i%D].add(sorted_indices[i])
    else:
        d_set[D-1-i%D].add(sorted_indices[i])

for qi in range(Q-cnt):
    print("1 1 1 2", flush=True)  # You are comparing two same fixed values in this loop.
    res = input()

d = [-1] * N
for i in range(D):
    for j in d_set[i]:
        d[j] = i

print(*d, flush=True)
