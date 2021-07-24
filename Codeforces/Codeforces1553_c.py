# http://codeforces.com/contest/1553/problem/C


def main():
    s = input().rstrip()
    cummax = [[0] for _ in range(2)]
    cummin = [[5] for _ in range(2)]
    for i in range(10):
        if s[i]=='0':
            cummax[i%2].append(cummax[i%2][-1])
        else:
            cummax[i%2].append(cummax[i%2][-1] + 1)
        if s[i]=='1':
            cummin[i%2].append(cummin[i%2][-1])
        else:
            cummin[i%2].append(cummin[i%2][-1] - 1)
    # print(cummax)
    # print(cummin)
    for i in range(10):
        b = i//2
        a = i-b
        if cummax[0][a]>cummin[1][b] or cummin[0][a]<cummax[1][b]:
            print(i)
            return
    print(10)
    return

t = int(input())
for i in range(t):
    main()
