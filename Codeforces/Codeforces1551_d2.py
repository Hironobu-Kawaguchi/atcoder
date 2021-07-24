# http://codeforces.com/contest/1551/problem/D1

from string import ascii_lowercase
# print(ascii_lowercase)

def main():
    n_org, m_org, k = map(int, input().split())
    n = n_org
    m = m_org
    ans = [['']*m for _ in range(n)]
    cnt = 0
    if n_org%2:
        if k<m_org//2:
            print("NO")
            return
        else:
            for i in range(m_org//2):
                ans[n_org-1][i*2] = ascii_lowercase[cnt]
                ans[n_org-1][i*2+1] = ascii_lowercase[cnt]
                cnt += 1
                cnt %= 26
            k -= m_org//2
            n -= 1
    if m_org%2:
        if (n_org*m_org//2)-k<n_org//2:
            print("NO")
            return
        else:
            for i in range(n_org//2):
                ans[i*2][m_org-1] = ascii_lowercase[cnt]
                ans[i*2+1][m_org-1] = ascii_lowercase[cnt]
                cnt += 1
                cnt %= 26
            m -= 1

    def ok(i, j, cnt):
        if i>0:
            if ans[i-1][j]==ascii_lowercase[cnt]: return False
            if ans[i-1][j+1]==ascii_lowercase[cnt]: return False
        if i<n_org-2:
            if ans[i+2][j]==ascii_lowercase[cnt]: return False
            if ans[i+2][j+1]==ascii_lowercase[cnt]: return False
        if j>0:
            if ans[i][j-1]==ascii_lowercase[cnt]: return False
            if ans[i+1][j-1]==ascii_lowercase[cnt]: return False
        if j<m_org-2:
            if ans[i][j+2]==ascii_lowercase[cnt]: return False
            if ans[i+1][j+2]==ascii_lowercase[cnt]: return False
        return True

    if n%2==0 and m%2==0:
        if k%2==0:
            print("YES")
            i2, j2 = 0, 0
            if n!=0 and m!=0:
                for x in range(k//2):
                    while not ok(i2, j2, cnt):
                        cnt += 1
                        cnt %= 26
                    ans[i2][j2] = ascii_lowercase[cnt]
                    ans[i2][j2+1] = ascii_lowercase[cnt]
                    cnt += 1
                    cnt %= 26
                    while not ok(i2, j2, cnt):
                        cnt += 1
                        cnt %= 26
                    ans[i2+1][j2] = ascii_lowercase[cnt]
                    ans[i2+1][j2+1] = ascii_lowercase[cnt]
                    cnt += 1
                    cnt %= 26
                    j2 += 2
                    if j2>m-1:
                        j2 = 0
                        i2 += 2
                while i2<n:
                    while not ok(i2, j2, cnt):
                        cnt += 1
                        cnt %= 26
                    ans[i2][j2] = ascii_lowercase[cnt]
                    ans[i2+1][j2] = ascii_lowercase[cnt]
                    cnt += 1
                    cnt %= 26
                    while not ok(i2, j2, cnt):
                        cnt += 1
                        cnt %= 26
                    # print(n, m, ans, i2, j2, cnt)
                    ans[i2][j2+1] = ascii_lowercase[cnt]
                    ans[i2+1][j2+1] = ascii_lowercase[cnt]
                    cnt += 1
                    cnt %= 26
                    j2 += 2
                    if j2>m-1:
                        j2 = 0
                        i2 += 2
            # print(ans)
            for ans_line in ans:
                print(''.join(ans_line))
        else:
            print("NO")
    return

t = int(input())
for i in range(t):
    main()
