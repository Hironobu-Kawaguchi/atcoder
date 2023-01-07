# https://atcoder.jp/contests/abc241/tasks/abc241_d
# https://atcoder.jp/contests/abc241/submissions/29726957
import sys
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, product, combinations_with_replacement, groupby, accumulate
import operator
from math import sqrt, gcd, factorial
#from math import isqrt, prod, comb  #python3.8用(notpypy)
#from bisect import bisect_left, bisect_right
#from functools import lru_cache, reduce
#from heapq import heappush, heappop, heapify, heappushpop, heapreplace
#import numpy as np
#import networkx as nx
#from networkx.utils import UnionFind
#from numba import njit, b1, i1, i4, i8, f8
#numba例 @njit(i1(i4[:], i8[:, :]),cache=True) 引数i4配列、i8 2次元配列,戻り値i1
#from scipy.sparse import csr_matrix
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, NegativeCycleError, maximum_bipartite_matching, maximum_flow, minimum_spanning_tree
def input(): return sys.stdin.readline().rstrip()
def divceil(n, k): return 1+(n-1)//k  # n/kの切り上げを返す
def yn(hantei, yes='Yes', no='No'): print(yes if hantei else no)

# 改造 https://ikatakos.com/pot/programming_algorithm/data_structure/trie
class BinaryTrie:

    def __init__(self, bit_depth):
        self.root = [None, None, 0]  # [0-child, 1-child, count]
        self.bit_start = 1 << (bit_depth - 1)

    def insert(self, x):
        """xを格納"""
        b = self.bit_start
        node = self.root
        node[2] += 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                node[i] = [None, None, 1]
            else:
                node[i][2] += 1
            node = node[i]
            b >>= 1

    def pop_min(self, mask=0):
        """xor_mask適用後の最小値を取得し、木からは削除"""
        b = self.bit_start
        node = self.root
        m = mask
        node[2] -= 1
        ret2 = 0
        while b:
            i = bool(m & b)
            ret2 = ret2 << 1
            if node[i] is None:
                i ^= 1
                ret2 += 1

            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1
        return ret2

    def get_min(self, mask=0):
        """xor_mask適用後の最小値を取得"""
        b = self.bit_start
        node = self.root
        m = mask
        ret2 = 0
        while b:
            i = bool(m & b)
            ret2 = ret2 << 1
            if node[i] is None:
                i ^= 1
                ret2 += 1
            node = node[i]
            b >>= 1
        return ret2

    def get_kth_min(self, k=1):
        """k番目に小さい値を取得"""
        b = self.bit_start
        node = self.root
        ret2 = 0
        while b:
            # print(b)
            ret2 = ret2 << 1
            b >>= 1
            if node[0] is None:
                node = node[1]
                ret2 += 1
                continue
            if node[1] is None:
                node = node[0]
                continue
            if k <= node[0][2]:
                node = node[0]
                continue
            else:
                k -= node[0][2]
                node = node[1]
                ret2 += 1
                continue
        return ret2

    def erase(self, x):
        """xを削除"""
        b = self.bit_start
        node = self.root
        node[2] -= 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i][2] > 1:
                node[i][2] -= 1
                node = node[i]
            else:
                tmp = node[i]
                node[i] = None
                node = tmp
            b >>= 1

    def lower_bound(self, bound=0):
        """boundより大きい値での最小値を取得。存在しない場合はNoneを返す。"""
        ans = self.get_kth_min(self.less_x(bound+1)+1)
        if ans > bound:
            return ans

    def upper_bound(self, bound=0):
        """boundより小さい値での最大値を取得。存在しない場合はNoneを返す。"""
        ans = self.get_kth_min(self.less_x(bound))
        if ans < bound:
            return ans

    def merge(self, trie):
        """2つのbinatytrie木を合成"""
        def merges(x, y):
            if (not x):
                return y
            if (not y):
                return x
            return [merges(x[0], y[0]), merges(x[1], y[1]), x[2]+y[2]]
        self.root = merges(self.root, trie.root)

    def less_x(self, x):
        """xより小さい値の数を出力"""
        if x < 0:
            return 0
        b = self.bit_start
        node = self.root
        ans = 0
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                if i == 1:
                    ans += node[0][2]
                return ans
            if i == 1:
                if node[0] is not None:
                    ans += node[0][2]
            node = node[i]
            b >>= 1
        return ans

    def less_x_mask(self, x, mask=0):
        """xormask適用後,xより小さい値の数を出力"""
        if x < 0:
            return 0
        b = self.bit_start
        node = self.root
        ans = 0
        m = mask
        # print(self.root)
        while b:
            i = bool(x & b)
            mm = bool(m & b)
            imm = i ^ mm
            if node[imm] is None:
                if i == 1:
                    ans += node[imm ^ 1][2]
                return ans
            if i == 1:
                if node[imm ^ 1] is not None:
                    ans += node[imm ^ 1][2]
            node = node[imm]
            b >>= 1
        return ans

    def is_exist(self, x):
        """xが存在するか判定"""
        b = self.bit_start
        node = self.root
        node[2] -= 1
        # print(self.root)
        while b:
            i = bool(x & b)
            if node[i] is None:
                return False
            node = node[i]
            b >>= 1
        return True

def main():
    mod = 10**9+7
    mod2 = 998244353
    bi=BinaryTrie(60)
    count=0
    for i in range(int(input())):
        query=list(map(int, input().split()))
        if query[0]==1:
            bi.insert(query[1])
            count+=1
        elif query[0]==2:
            num=bi.less_x(query[1]+1)
            if num < query[2]:
                print(-1)
            else:
                print(bi.get_kth_min(num-query[2]+1))
        else:
            num=bi.less_x(query[1])
            if num + query[2] > count:
                print(-1)
            else:
                print(bi.get_kth_min(num+query[2]))


if __name__ == '__main__':
    main()
