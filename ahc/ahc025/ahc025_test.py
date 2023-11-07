# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

import sys
import math

N, D, Q = map(int, input().split())
W = list(map(int, input().split()))
sorted_indices = sorted(range(N), key=lambda x: W[x], reverse=True)
print(*sorted_indices)

def compare(l_index, r_index):
    if type(l_index) == int:
        l_sum = W[l_index]
        r_sum = W[r_index]
    else:
        l_sum = sum(W[i] for i in l_index)
        r_sum = sum(W[i] for i in r_index)
    if l_sum == r_sum:
        return 0
    elif l_sum > r_sum:
        return -1
    else:
        return 1


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        comparison = compare(left[i], right[j])
        # 昇順に並べる
        if comparison >= 0:   # left[i] <= right[j]
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(indices):
    if len(indices) <= 1:
        return indices

    mid = len(indices) // 2
    left = merge_sort(indices[:mid])
    right = merge_sort(indices[mid:])

    return merge(left, right)

def make_ans(hb):
    # hb: HappyBags
    ans = [-1] * N
    for i in range(D):
        for j in hb[i]:
            ans[j] = i
    return ans

def check_happy(hb):
    for i in range(D):
        tmp = 0
        for j in hb[i]:
            tmp += W[j]
        print(i, tmp, sorted(hb[i]), sorted([W[i] for i in hb[i]], reverse=True), file=sys.stderr)


# Q回以内にソート可能なgroupのサイズを決める
group_size = 1
while True:
    group_num = (N + group_size - 1) // group_size
    if group_num * math.ceil(math.log2(group_num)) <= Q:
        break
    group_size += 1
group_num = (N + group_size - 1) // group_size
print(group_size, group_num, file=sys.stderr)

group = [set() for _ in range(group_num)]
for i in range(N):
    group[i%group_num].add(i)
sorted_group = merge_sort(group)


HappyBags = [set() for _ in range(D)]
# for i in range(N):
#     HappyBags[i%D].add(i)
for i in range(group_num):
    j = group_num - i - 1
    if (j//D)%2 == 0:
        HappyBags[j%D] |= sorted_group[i]
    else:
        HappyBags[D-1-j%D] |= sorted_group[i]


while True:
    check_happy(HappyBags)
    print("#c", *make_ans(HappyBags), flush=True)
    HappyBags = merge_sort(HappyBags)
    check_happy(HappyBags)
    print("#c", *make_ans(HappyBags), flush=True)
    # 一番大きいBagから一番小さいBagに移動しても大小が逆転しない最大のグッズを探し、移動する
    r_sorted_indices = merge_sort(list(HappyBags[-1]))
    move_ok_idx = -1
    for i in range(len(r_sorted_indices)):
        move_set = set([r_sorted_indices[i]])
        new_big_set = HappyBags[-1] - move_set
        new_small_set = HappyBags[0] | move_set
    #     if ci.cnt_queries >= Q: break
    #     if ci.compare(new_big_set, new_small_set) >= 0: # 大小が逆転しない
    #         move_ok_idx = i
    #     else:
    #         break
    # if move_ok_idx == -1:
    #     break
    move_set = set([r_sorted_indices[move_ok_idx]])
    HappyBags[0] = HappyBags[0] | move_set
    HappyBags[-1] = HappyBags[-1] - move_set
    break


# print(ci.cnt_queries, ci.cnt_use_memos, file=sys.stderr)
# print(*d, flush=True)
print(*make_ans(HappyBags), flush=True)
