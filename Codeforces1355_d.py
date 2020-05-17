# https://codeforces.com/contest/1355/problem/D

def main():
    n,s = map(int, input().split())
    if 2*n <= s:
        print('YES')
        ans = [2]*(n-1)
        ans.append(s-2*(n-1))
        print(*ans)
        print(1)
    else:
        print('NO')
    return

main()
