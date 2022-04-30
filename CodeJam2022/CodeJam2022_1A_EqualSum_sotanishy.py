import sys
input = sys.stdin.readline

def solve(q):
    N = int(input())
    A = []
    st = set()
    for i in range(30):
        A.append(1<<i)
        st.add(1<<i)
    i = 1
    while len(st) < N:
        if i not in st:
            A.append(i)
            st.add(i)
        i += 1
    A.sort()
    print(*A, flush=True)
    B = list(map(int, input().split()))
    A += B
    ans = []
    fsum, ssum = 0, A[2*N-1]
    for i in range(2*N-1)[::-1]:
        if abs(fsum+A[i]-ssum) < abs(fsum-ssum-A[i]):
            ans.append(A[i])
            fsum += A[i]
        else:
            ssum += A[i]
    print(*ans, flush=True)

T = int(input())
for t in range(T):
    solve(t+1)