# https://atcoder.jp/contests/ahc015/tasks/ahc015_a
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# from numba import njit
# from functools import lru_cache

import sys
input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
from collections import Counter, deque
import copy
import random

N = 100
cand = ['L', 'B', 'R', 'F']
pos_ans = [-1]*100
iter_count = 10

f = list(map(int, (input().split())))
cnt = Counter(f)
# print(cnt)
cnt_sort = sorted([(v, k) for k, v in cnt.items()], reverse=True)
# print(cnt_sort)


def cycle(pos):
    new_pos = [-1]*100
    for i in range(10):
        for j in range(10):
            new_pos[j*10+9-i] = pos[i*10+j]
    return new_pos

def left(pos):
    new_pos = [-1]*100
    lst = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if pos[i*10+j]!=-1:
                lst[i].append(pos[i*10+j])
    for i in range(10):
        for j, x in enumerate(lst[i]):
            new_pos[i*10+j] = x
    return new_pos

def new_p(p, pos):
    for i in range(N):
        if pos[i]==-1:
            p -= 1
        if p==0:
            return i + 1

def compute_score(pos):
    connected_components = []
    ds = [0] * 4
    v = [-1, 1, -10, 10]
    done = [False] * N
    for i in range(N):
        if pos[i]!=-1:
            ds[pos[i]] += 1
        if done[i]: continue
        cnt = 1
        done[i] = True
        q = deque()
        q.append(i)
        while len(q):
            next = q.popleft()
            for d in v:
                if next%10==0 and d==-1: continue
                if (next+1)%10==0 and d==1: continue
                if 0<=next+d<N and pos[next+d]==pos[next] and done[next+d]==False:
                    q.append(next+d)
                    done[next+d] = True
                    cnt += 1
        connected_components.append(cnt)
    # print(pos)
    # print(connected_components)
    numerator = 0
    for x in connected_components:
        numerator += x*x
    denominator = 0
    for i in range(1,4):
        denominator += ds[i]*ds[i]
    return round(1000000 * numerator / denominator)

def compute_point(pos):
    ret = 0
    lst = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if pos[i*10+j]!=-1:
                lst[i].append(pos[i*10+j])
                if len(lst[i])>=2 and lst[i][-1]==lst[i][-2]:
                    ret += 1
    for i in range(9):
        for j in range(10):
            if len(lst[i])>j and len(lst[i+1])>j:
                if lst[i][j]==lst[i+1][j]:
                    ret += 1
    # new_pos = cycle(pos)
    # lst = [[] for _ in range(10)]
    # for i in range(10):
    #     for j in range(10):
    #         if new_pos[i*10+j]!=-1:
    #             lst[i].append(new_pos[i*10+j])
    #             if len(lst[i])>=2 and lst[i][-1]==lst[i][-2]:
    #                 ret += 1
    # for i in range(9):
    #     for j in range(10):
    #         if len(lst[i])>j and len(lst[i+1])>j:
    #             if lst[i][j]==lst[i+1][j]:
    #                 ret += 1
    return ret

def search(pos):
    new_pos = copy.copy(pos)
    # score = compute_point(new_pos)
    # score = compute_score(new_pos)
    score = compute_point(new_pos) * compute_score(new_pos)
    best_idx = 0
    # print(0, score)
    for i in range(1, 4):
        new_pos = cycle(new_pos)
        # new_score = compute_point(new_pos)
        new_score = compute_point(new_pos) * compute_score(new_pos)
        if new_score>score:
            score = new_score
            best_idx = i
        # print(i, score)
    # print(best_idx, score, pos)
    return best_idx

def simulation(t, pos):
    new_pos = copy.copy(pos)
    for i in range(t, N):
        p = random.randrange(1, N-i+1)
        np = new_p(p, new_pos)
        # print(p, np, i)
        new_pos[np-1] = f[i]
        # idx = random.randrange(4)
        idx = search(new_pos)
        for i in range(idx):
            new_pos = cycle(new_pos)
        new_pos = left(new_pos)
        for i in range(4-idx):
            new_pos = cycle(new_pos)
    # return compute_score(new_pos) * compute_point(pos)
    return compute_score(new_pos)

def random_simulation(t, pos):
    new_pos = copy.copy(pos)
    for i in range(t, N):
        p = random.randrange(1, N-i+1)
        np = new_p(p, new_pos)
        # print(p, np, i)
        new_pos[np-1] = f[i]
        idx = random.randrange(4)
        for i in range(idx):
            new_pos = cycle(new_pos)
        new_pos = left(new_pos)
        for i in range(4-idx):
            new_pos = cycle(new_pos)
    # return compute_score(new_pos) * compute_point(pos)
    return compute_score(new_pos)

def mcmc(t, pos):
    new_pos = copy.copy(pos)
    best_idx = -1
    best_score = 0
    for k in range(4):
        sum_score = 0
        for i in range(k):
            new_pos = cycle(new_pos)
        new_pos = left(new_pos)
        for i in range(4-k):
            new_pos = cycle(new_pos)
        # for i in range(iter_count):
        for i in range((N-t)+1):
        # for i in range((N-t)*(N-t)+1):
            # print(random_simulation(0, pos_ans))
            # sum_score += random_simulation(t+1, pos_ans)
            sum_score += simulation(t+1, pos_ans)
        # print(cand[k], sum_score)
        if sum_score>best_score:
            best_idx = k
            best_score = sum_score
    return best_idx
        
for i in range(N):
    # if i==0:
    #     print('L', flush=True)
    #     continue
    p = int(input())
    np = new_p(p, pos_ans)
    # print(p, np)
    pos_ans[np-1] = f[i]

    best_idx = search(pos_ans)
    # if i<90:
    #     best_idx = search(pos_ans)
    # else:
    #     best_idx = mcmc(i, pos_ans)
    print(cand[best_idx], flush=True)

    for i in range(best_idx):
        pos_ans = cycle(pos_ans)
    pos_ans = left(pos_ans)
    for i in range(4-best_idx):
        pos_ans = cycle(pos_ans)

    # print('F', flush=True)
    # for i in range(4):
    #     pos = cycle(pos)
    # print(pos)

    # if f[p-1]==cnt_sort[0][1]:
    #     print('F', flush=True)
    # # elif f[p-1]==2:
    # #     print('L', flush=True)
    # else:
    #     # print('L', flush=True)
    #     print('F', flush=True)

print(compute_score(pos_ans))
