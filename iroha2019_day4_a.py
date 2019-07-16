# A - あるよるのできごと
# https://atcoder.jp/contests/iroha2019-day4/tasks/iroha2019_day4_a

N, A, B, C, D = map(int, input().split())
A = list(map(int, input().split())) + [-1]
B = list(map(int, input().split())) + [-1]
C = list(map(int, input().split())) + [-1]
D = list(map(int, input().split())) + [-1]


def solve(N, ia, ib, ic, id):
    #print(N, ia, ib, ic, id)
    a, b, c, d = A[ia], B[ib], C[ic], D[id]
    if a==b==c==d==-1:
        if N==0:
            return []
        else:
            return False
    elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        return False
    elif [a, b, c, d].count(-1) > 1:
        return False
    elif [a, b, c, d].count(1)>2 or [a, b, c, d].count(2)>2 or [a, b, c, d].count(3)>2:
        return False
    elif sorted([a,b,c,d])==[-1,1,2,3]:
        if a==-1:
            s = solve(N-1, ia, ib+1, ic+1, id+1)
            return False if s==False else [1] + s
        elif b==-1:
            s = solve(N-1, ia+1, ib, ic+1, id+1)
            return False if s==False else [2] + s
        elif c == -1:
            s = solve(N-1, ia+1, ib+1, ic, id+1)
            return False if s == False else [3] + s
        elif d == -1:
            s = solve(N-1, ia+1, ib+1, ic+1, id)
            return False if s == False else [4] + s
    elif [a, b, c, d].count(-1) == 1:
        return False
    elif a==b:
        s = solve(N-1, ia, ib+1, ic+1, id+1)
        if s!=False:
            return [1] + s
        s = solve(N-1, ia+1, ib, ic+1, id+1)
        if s!=False:
            return [2] + s
        return False
    elif a==c:
        s = solve(N-1, ia, ib+1, ic+1, id+1)
        if s!=False:
            return [1] + s
        s = solve(N-1, ia+1, ib+1, ic, id+1)
        if s!=False:
            return [3] + s
        return False
    elif a==d:
        s = solve(N-1, ia, ib+1, ic+1, id+1)
        if s!=False:
            return [1] + s
        s = solve(N-1, ia+1, ib+1, ic+1, id)
        if s!=False:
            return [4] + s
        return False
    elif b==c:
        s = solve(N-1, ia+1, ib, ic+1, id+1)
        if s!=False:
            return [2] + s
        s = solve(N-1, ia+1, ib+1, ic, id+1)
        if s!=False:
            return [3] + s
        return False
    elif b==d:
        s = solve(N-1, ia+1, ib, ic+1, id+1)
        if s!=False:
            return [2] + s
        s = solve(N-1, ia+1, ib+1, ic+1, id)
        if s!=False:
            return [4] + s
        return False
    elif c==d:
        s = solve(N-1, ia+1, ib+1, ic, id+1)
        if s!=False:
            return [3] + s
        s = solve(N-1, ia+1, ib+1, ic+1, id)
        if s!=False:
            return [4] + s
        return False

    assert False

s = solve(N, 0,0,0,0)
if s != False:
    print("Yes")
    print(*s, sep="\n")
else:
    print("No")


"""
# import itertools
N, A, B, C, D = map(int, input().split())
ns = [A, B, C, D]
a = list(input().split())
b = list(input().split())
c = list(input().split())
d = list(input().split())

def chk(a, b, c, d, ii, ans):
    tmps = []
    if len(a) == 0 and len(b) == 0 and len(c) == 0 and len(d) == 0:
        print('No')
        return 0, []    # 該当なし
    elif ns[0] - ii[0] -1 == 0:
        abcd = b[ii[1]] + c[ii[2]] + d[ii[3]]
        ans.append(1)
        return 1, ans
    elif ns[1] - ii[1] -1 == 0:
        abcd = a[ii[0]] + c[ii[2]] + d[ii[3]]
        ans.append(2)
        return 1, ans
    elif ns[2] - ii[2] -1 == 0:
        abcd = a[ii[0]] + b[ii[1]] + d[ii[3]]
        ans.append(3)
        return 1, ans
    elif ns[3] - ii[3] -1 == 0:
        abcd = a[ii[0]] + b[ii[1]] + c[ii[2]]
        ans.append(4)
        return 1, ans
    else:
        abcd = a[ii[0]] + b[ii[1]] + c[ii[2]] + d[ii[3]]

    if abcd.count('1') == 2 or abcd.count('2') == 2 or abcd.count('3') == 2:
        abcdx = int(abcd[0]) * int(abcd[1]) * int(abcd[2]) * int(abcd[3])
        if abcdx % 6 == 0:  # 1,2,3が1回以上出てくる
            xx = str(abcdx // 6)
            for i in range(4):
                if abcd[i] == xx:
                    tmps.append(i+1)
                    for j in range(4):
                        if i == j:
                            continue
                        else:
                            if ii[j] < ns[j]-1:
                                ii[j] += 1
                    status, tmps = chk(a, b, c, d, ii, ans)
                    ans += tmps
            return 2, tmps
    else:
        return 0, []    # 該当なし

ans = []
ii = [0, 0, 0, 0]
status, tmps = chk(a, b, c, d, ii, ans)
print(status, ans)

if status == 1:
    print('Yes')
    for an in ans:
        print(an)
else:
    print('No')


# abcd = '1' * (N-A) + '2' * (N-B) + '3' * (N-C) + '4' * (N-D)
# cnt = 0
# for i in itertools.permutations(abcd, N):
#     cnt += 1

# print(cnt)
"""