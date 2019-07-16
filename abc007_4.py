# D - 禁止された数字
# https://atcoder.jp/contests/abc007/tasks/abc007_4
# a*10**n には (a!=4,9)*8**n の大丈夫な数があるので、禁止は(10**n - 8**n)

A, B = map(int, input().split())
d = {'0':'0',
     '1':'1',
     '2':'2',
     '3':'3',
     '4':'3',
     '5':'4',
     '6':'5',
     '7':'6',
     '8':'7',
     '9':'7',
    }
def ok(n):
    tmp = ''
    ns = str(n)
    keta = len(ns)
    flg = False
    for i in range(keta):
        if flg == True:
            tmp += '7'
        else:
            tmp += d[ns[i]]

        if ns[i] == '9' or ns[i] == '4':
            flg = True
    cnt = int(tmp, 8)
    return cnt

ans = ( B - ok(B)) - (A-1 - ok(A-1))
print(ans)


cnt = 0
for i in range(A, B+1):
    x = str(i)
    if '4' in x or '9' in x:
        cnt += 1
print(cnt)
