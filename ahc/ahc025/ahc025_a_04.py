# https://atcoder.jp/contests/ahc025/tasks/ahc025_a

import sys

N, D, Q = map(int, input().split())

# CompareItems classを作成
class CompareItems():
    def __init__(self, max_queries):
        self.max_queries = max_queries
        self.cnt_queries = 0
        self.cnt_use_memos = 0
        self.memo = {}

    def compare(self, l_index, r_index):
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
        # メモを使う
        if (l_tuple, r_tuple) in self.memo:
            self.cnt_use_memos += 1
            return self.memo[(l_tuple, r_tuple)]
        nl = len(l_tuple)
        nr = len(r_tuple)
        if nl == 0 and nr == 0:
            return 0
        elif nl == 0:
            return 1
        elif nr == 0:
            return -1

        # クエリを投げる
        if self.cnt_queries >= self.max_queries:
            return 0
        print(nl, nr, *l_tuple, *r_tuple, flush=True)
        self.cnt_queries += 1
        result = input()        
        if result == "<":
            return 1
        elif result == "=":
            return 0
        elif result == ">":
            return -1
        return 0


def merge(left, right, ci):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        comparison = ci.compare(left[i], right[j])
        if comparison <= 0:
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


# ここからメイン処理
ci = CompareItems(Q)
cnt = 0
indices = list(range(N))
sorted_indices = merge_sort(indices, ci)

d_set = [set() for _ in range(D)]
for i in range(N):
    if (i//D)%2 == 0:
        d_set[i%D].add(sorted_indices[i])
    else:
        d_set[D-1-i%D].add(sorted_indices[i])

for qi in range(Q - ci.cnt_queries):
    print("1 1 1 2", flush=True)  # You are comparing two same fixed values in this loop.
    res = input()

d = [-1] * N
for i in range(D):
    for j in d_set[i]:
        d[j] = i

print(ci.cnt_queries, ci.cnt_use_memos, file=sys.stderr)
print(*d, flush=True)
