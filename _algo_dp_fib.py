# 動的計画法（Dynamic Programming）
# https://www.jabba.cloud/20161020172918/
# https://qiita.com/takey/items/4b1767af0f0652ef8764

# -*- coding: utf-8 -*-
def fib(n):
    """フィボナッチ数列"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_memo(n):
    """メモ化フィボナッチ"""
    memo = [0]*(n+1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != 0:
            return memo[n]
        memo[n] = _fib(n-1) + _fib(n-2)
        return memo[n]

    return _fib(n)

import time
n = 20
print("n = ", n)

def do_fib():
    start = time.time()
    print(fib(n))
    stop = time.time()
    print("elapsed: {}".format(stop - start))

def do_fib_memo():
    start = time.time()
    print(fib_memo(n))
    stop = time.time()
    print("elapsed: {}".format(stop - start))

if __name__ == '__main__':
    do_fib()
    do_fib_memo()
