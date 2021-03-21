# https://codeforces.com/contest/1265/problem/D

def main():
    abcd = list(map(int, input().split()))
    sm = sum(abcd)
    mx = 0
    for i in range(4):
        if i in [0, 3]:
            tmp = abcd[i] * 2
        else:
            tmp = abcd[i]
        if tmp > mx:
            start = i
            mx = tmp
    l = [start]
    abcd[start] -= 1
    i = start
    while len(l) < sm:
        if i == 0:
            i += 1
            if abcd[i] == 0:
                print("NO")
                return
            else:
                l.append(i)
                abcd[i] -= 1
        elif i == 1:
            if abcd[i-1]*2 >= abcd[i+1]:
                i -= 1
                if abcd[i] == 0:
                    print("NO")
                    return
                else:
                    l.append(i)
                    abcd[i] -= 1
            else:
                i += 1
                if abcd[i] == 0:
                    print("NO")
                    return
                else:
                    l.append(i)
                    abcd[i] -= 1
        elif i == 2:
            if abcd[i+1]*2 >= abcd[i-1]:
                i += 1
                if abcd[i] == 0:
                    print("NO")
                    return
                else:
                    l.append(i)
                    abcd[i] -= 1
            else:
                i -= 1
                if abcd[i] == 0:
                    print("NO")
                    return
                else:
                    l.append(i)
                    abcd[i] -= 1
        elif i == 3:
            i -= 1
            if abcd[i] == 0:
                print("NO")
                return
            else:
                l.append(i)
                abcd[i] -= 1
    print("YES")
    print(*l)

main()