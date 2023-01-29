# https://atcoder.jp/contests/arc141/tasks/arc141_a

def main():
    S = input()
    N = int(S)
    k = len(S)
    cand = [10**(k-1)-1, 11]
    for a in range(1, k//2+1):
        tmp = int(S[:a]*(k//a))
        if tmp<=N:
            cand.append(tmp)
        cand.append(int(str((int(S[:a])-1))*(k//a)))
    cand.sort(reverse=True)
    # print(cand)
    print(cand[0])

T = int(input())
for ti in range(T):
    main()


# import sys
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)
# def main():
#     S = input()
#     candidates = []
#     for i in range(1, len(S)):
#         if len(S)%i: continue
#         candidate = S[:i] * (len(S)//i)
#         if int(candidate)<=int(S): candidates.append(int(candidate))
#         if int(S[:i])>=2 and len(S[:i])==len(str(int(S[:i])-1)):
#             candidate = (str(int(S[:i])-1)) * (len(S)//i)
#             if int(candidate)<=int(S): candidates.append(int(candidate))
#     candidates.sort(reverse=True)
#     # print(candidates)
#     if len(candidates)==0:
#         return '9'*(len(S)-1)
#     return candidates[0]

# T = int(input())
# for ti in range(T):
#     print(main())

