# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

import sys
import math

N, D, Q = map(int, input().split())

# CompareItems classを作成
class CompareItems():
    def __init__(self, max_queries):
        self.max_queries = max_queries
        self.cnt_queries = 0
        self.cnt_use_memos = 0
        self.memo = {}

    def compare(self, l_index, r_index):
        sign = 1
        if type(l_index) != set:
            if type(l_index) == int:
                l_index = set([l_index])
            else:
                l_index = set(l_index)
        if type(r_index) != set:
            if type(r_index) == int:
                r_index = set([r_index])
            else:
                r_index = set(r_index)
        sekisetsu = l_index & r_index
        l_index -= sekisetsu
        r_index -= sekisetsu
        l_tuple = tuple(sorted(l_index))
        r_tuple = tuple(sorted(r_index))
        if l_tuple == r_tuple:
            return 0
        elif l_tuple > r_tuple:
            l_tuple, r_tuple = r_tuple, l_tuple
            sign = -1
        # メモを使う
        if (l_tuple, r_tuple) in self.memo:
            self.cnt_use_memos += 1
            print("# use memo", len(l_tuple), len(r_tuple), *l_tuple, *r_tuple, flush=True)
            result = self.memo[(l_tuple, r_tuple)] * sign
            print("# result: ", result, flush=True)
            return result
        
        nl = len(l_tuple)
        nr = len(r_tuple)
        if nl == 0 and nr == 0:
            return 0
        elif nl == 0:
            return 1 * sign
        elif nr == 0:
            return -1 * sign
        if self.cnt_queries >= self.max_queries:
            return 0
        # クエリを投げる
        print(nl, nr, *l_tuple, *r_tuple, flush=True)
        self.cnt_queries += 1
        result = input()
        if result == "<":
            result = 1 * sign
        elif result == "=":
            result = 0
        elif result == ">":
            result = -1 * sign
        else:
            result = 0
        self.memo[(l_tuple, r_tuple)] = result * sign   # メモを更新
        print("# result: ", result, flush=True)
        return result


def merge(left, right, ci):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        comparison = ci.compare(left[i], right[j])
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

def merge_sort(indices, ci):
    if len(indices) <= 1:
        return indices

    mid = len(indices) // 2
    left = merge_sort(indices[:mid], ci)
    right = merge_sort(indices[mid:], ci)

    return merge(left, right, ci)

def make_ans(hb):
    # hb: HappyBags
    ans = [-1] * N
    for i in range(D):
        for j in hb[i]:
            ans[j] = i
    return ans


# ここからメイン処理
ci = CompareItems(Q)

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
sorted_group = merge_sort(group, ci)


HappyBags = [set() for _ in range(D)]
# for i in range(N):
#     HappyBags[i%D].add(i)
for i in range(group_num):
    j = group_num - i - 1
    if (j//D)%2 == 0:
        HappyBags[j%D] |= sorted_group[i]
    else:
        HappyBags[D-1-j%D] |= sorted_group[i]


while ci.cnt_queries < Q:
    print("#c", *make_ans(HappyBags), flush=True)
    HappyBags = merge_sort(HappyBags, ci)
    # print(HappyBags, file=sys.stderr)
    print("#c", *make_ans(HappyBags), flush=True)
    # 一番大きいBagから一番小さいBagに移動しても大小が逆転しない最大のグッズを探し、移動する
    r_sorted_indices = merge_sort(list(HappyBags[-1]), ci)
    move_ok_idx = -1
    for i in range(len(r_sorted_indices)):
        move_set = set([r_sorted_indices[i]])
        new_small_set = HappyBags[0] | move_set
        new_big_set = HappyBags[-1] - move_set
        if ci.cnt_queries >= Q: break
        if ci.compare(new_small_set, new_big_set) >= 0: # 大小が逆転しない
            move_ok_idx = i
        else:
            break
    if move_ok_idx == -1:
        print("# no move", flush=True)
        break
    move_set = set([r_sorted_indices[move_ok_idx]])
    print("# move", r_sorted_indices[move_ok_idx], flush=True)
    HappyBags[0] = HappyBags[0] | move_set
    HappyBags[-1] = HappyBags[-1] - move_set


# Q回まで適当なクエリを投げる
for qi in range(Q - ci.cnt_queries):
    print("1 1 1 2", flush=True)  # You are comparing two same fixed values in this loop.
    res = input()

print(ci.cnt_queries, ci.cnt_use_memos, file=sys.stderr)
# print(*d, flush=True)
print(*make_ans(HappyBags), flush=True)
