# https://atcoder.jp/contests/arc155/tasks/arc155_b

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True
    
    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

def main():
    Q, A, B = map(int, input().split())
    SS = SortedSet()
    INF = 1<<60
    SS.add(A-B)
    SS.add(A+B)
    SS.add(INF)
    SS.add(-INF)
    for qi in range(Q):
        t, a, b = map(int, input().split())
        if t==1:
            SS.add(a-b)
            SS.add(a+b)
        else:
            a0 = SS.le(a)
            a1 = SS.ge(a)
            b0 = SS.le(b)
            b1 = SS.ge(b)
            # print(a, a0, a1, b, b0, b1)
            if a1<=b0:
                print(0)
                continue
            print(min(a-a0, a1-a, b-b0, b1-b))
    return

main()




# TLE
# def main():
#     Q, A, B = map(int, input().split())
#     T = set([A-B, A+B])
#     for qi in range(Q):
#         t, a, b = map(int, input().split())
#         if t==1:
#             T.add(a-b)
#             T.add(a+b)
#         else:
#             lst = sorted(list(T))
#             # print(a, b, lst)
#             idx_a = bisect.bisect_left(lst, a)
#             idx_b = bisect.bisect_right(lst, b)
#             # print(idx_a, idx_b, lst)
#             if idx_a!=idx_b:
#                 print(0)
#             else:
#                 ans = 1001001001
#                 if idx_a!=0:
#                     ans = min(ans, a - lst[idx_a - 1])
#                 if idx_b<len(lst):
#                     ans = min(ans, lst[idx_b] - b)
#                 print(ans)
#     return

# main()


# TLE
# import sys
# input = sys.stdin.buffer.readline
# # def input(): return sys.stdin.readline().rstrip()
# # sys.setrecursionlimit(10 ** 7)

# def f(x, a, b):
#     return abs(abs(x-a)-b)

# def main():
#     Q, A, B = map(int, input().split())
#     T = set([(A, B)])
#     for qi in range(Q):
#         t, a, b = map(int, input().split())
#         if t==1:
#             T.add((a, b))
#         else:
#             ans = 1001001001
#             for aa, bb in T:
#                 ans = min(ans, f(a, aa, bb))
#                 ans = min(ans, f(b, aa, bb))
#                 if a<aa-bb<b:
#                     ans = min(ans, f(aa-bb, aa, bb))
#                 if a<aa+bb<b:
#                     ans = min(ans, f(aa+bb, aa, bb))
#             print(ans)
#     return

# main()
