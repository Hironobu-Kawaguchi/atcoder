# # https://atcoder.jp/contests/abc308/tasks/abc308_f
# # from numba import njit
# # from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)
import heapq

N, M = map(int, (input().split()))
P = list(map(int, (input().split())))
P.sort()
print(P, file=sys.stderr)
L = list(map(int, (input().split())))
D = list(map(int, (input().split())))
dl = [[L[i], -D[i]] for i in range(M)]
dl.sort()
print(dl, file=sys.stderr)

ans = 0
for i in range(N):
    ans += P[i]

q = []
idx = 0
for i in range(N):
    while idx<M and dl[idx][0]<=P[i]:
        heapq.heappush(q, (dl[idx][1], dl[idx][0]))
        idx += 1
    while q:
        d, l = heapq.heappop(q)
        if P[i]>=l:
            print(ans, i, P[i], l, d, file=sys.stderr)
            ans += d
            break

print(ans)

# # https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
# import math
# from bisect import bisect_left, bisect_right
# from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
# T = TypeVar('T')
# class SortedMultiset(Generic[T]):
#     BUCKET_RATIO = 50
#     REBUILD_RATIO = 170

#     def _build(self, a: Optional[List[T]] = None) -> None:
#         "Evenly divide `a` into buckets."
#         if a is None: a = list(self)
#         size = len(a)
#         bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
#         self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
#     def __init__(self, a: Iterable[T] = []) -> None:
#         "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
#         a = list(a)
#         self.size = len(a)
#         if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
#             a = sorted(a)
#         self._build(a)

#     def __iter__(self) -> Iterator[T]:
#         for i in self.a:
#             for j in i: yield j

#     def __reversed__(self) -> Iterator[T]:
#         for i in reversed(self.a):
#             for j in reversed(i): yield j
    
#     def __eq__(self, other) -> bool:
#         return list(self) == list(other)
    
#     def __len__(self) -> int:
#         return self.size
    
#     def __repr__(self) -> str:
#         return "SortedMultiset" + str(self.a)
    
#     def __str__(self) -> str:
#         s = str(list(self))
#         return "{" + s[1 : len(s) - 1] + "}"

#     def _position(self, x: T) -> Tuple[List[T], int]:
#         "Find the bucket and position which x should be inserted. self must not be empty."
#         for a in self.a:
#             if x <= a[-1]: break
#         return (a, bisect_left(a, x))

#     def __contains__(self, x: T) -> bool:
#         if self.size == 0: return False
#         a, i = self._position(x)
#         return i != len(a) and a[i] == x

#     def count(self, x: T) -> int:
#         "Count the number of x."
#         return self.index_right(x) - self.index(x)

#     def add(self, x: T) -> None:
#         "Add an element. / O(√N)"
#         if self.size == 0:
#             self.a = [[x]]
#             self.size = 1
#             return
#         a, i = self._position(x)
#         a.insert(i, x)
#         self.size += 1
#         if len(a) > len(self.a) * self.REBUILD_RATIO:
#             self._build()
    
#     def _pop(self, a: List[T], i: int) -> T:
#         ans = a.pop(i)
#         self.size -= 1
#         if not a: self._build()
#         return ans

#     def discard(self, x: T) -> bool:
#         "Remove an element and return True if removed. / O(√N)"
#         if self.size == 0: return False
#         a, i = self._position(x)
#         if i == len(a) or a[i] != x: return False
#         self._pop(a, i)
#         return True

#     def lt(self, x: T) -> Optional[T]:
#         "Find the largest element < x, or None if it doesn't exist."
#         for a in reversed(self.a):
#             if a[0] < x:
#                 return a[bisect_left(a, x) - 1]

#     def le(self, x: T) -> Optional[T]:
#         "Find the largest element <= x, or None if it doesn't exist."
#         for a in reversed(self.a):
#             if a[0] <= x:
#                 return a[bisect_right(a, x) - 1]

#     def gt(self, x: T) -> Optional[T]:
#         "Find the smallest element > x, or None if it doesn't exist."
#         for a in self.a:
#             if a[-1] > x:
#                 return a[bisect_right(a, x)]

#     def ge(self, x: T) -> Optional[T]:
#         "Find the smallest element >= x, or None if it doesn't exist."
#         for a in self.a:
#             if a[-1] >= x:
#                 return a[bisect_left(a, x)]
    
#     def __getitem__(self, i: int) -> T:
#         "Return the i-th element."
#         if i < 0:
#             for a in reversed(self.a):
#                 i += len(a)
#                 if i >= 0: return a[i]
#         else:
#             for a in self.a:
#                 if i < len(a): return a[i]
#                 i -= len(a)
#         raise IndexError
    
#     def pop(self, i: int = -1) -> T:
#         "Pop and return the i-th element."
#         if i < 0:
#             for a in reversed(self.a):
#                 i += len(a)
#                 if i >= 0: return self._pop(a, i)
#         else:
#             for a in self.a:
#                 if i < len(a): return self._pop(a, i)
#                 i -= len(a)
#         raise IndexError

#     def index(self, x: T) -> int:
#         "Count the number of elements < x."
#         ans = 0
#         for a in self.a:
#             if a[-1] >= x:
#                 return ans + bisect_left(a, x)
#             ans += len(a)
#         return ans

#     def index_right(self, x: T) -> int:
#         "Count the number of elements <= x."
#         ans = 0
#         for a in self.a:
#             if a[-1] > x:
#                 return ans + bisect_right(a, x)
#             ans += len(a)
#         return ans
    
# N, M = map(int, (input().split()))
# P = list(map(int, (input().split())))
# SS = SortedMultiset()
# for i in range(N):
#     SS.add(P[i])
# # print(len(SS))
# # P.sort()
# # print(P)
# L = list(map(int, (input().split())))
# D = list(map(int, (input().split())))
# dl = [[D[i], L[i]] for i in range(M)]
# dl.sort(reverse=True)
# # print(dl)

# # used = [False] * N
# ans = 0
# for i in range(N):
#     ans += P[i]

# for i in range(M):
#     d, l = dl[i]
#     # print(d, l)
#     # idx = bisect.bisect_left(P, l)
#     idx = SS.index(l)
#     # while idx<N and used[idx]:
#     #     idx += 1
#     if idx==len(SS): continue
#     v = SS[idx]
#     SS.discard(v)
#     # used[idx] = True
#     # print(ans, d, l, idx, v)
#     ans -= d

# print(ans)

