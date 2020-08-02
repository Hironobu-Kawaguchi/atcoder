# https://atcoder.jp/contests/abc144/tasks/abc144_e


def main():
    import heapq
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) <= K:
        print(0)
        return

    F = list(map(int, input().split()))

    A.sort()
    F.sort(reverse=True)
    q = []
    for i in range(N):
        heapq.heappush(q, (-(A[i]*F[i]), A[i], F[i]))

    k = K
    while k > 0:
        p, a, f = heapq.heappop(q)
        if p < 0:
            nextp = q[0][0]
            tmp = min(min(max((nextp-p+f-1)//f, 1), k), a)
            heapq.heappush(q, ((-(a-tmp)*f), a-tmp, f))
            k -= tmp
        else:
            break

    p, a, f = heapq.heappop(q)
    print(-p)
    return

main()