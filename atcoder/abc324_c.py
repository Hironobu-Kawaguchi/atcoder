# https://atcoder.jp/contests/abc324/tasks/abc324_c

# import sys
# input = sys.stdin.buffer.readline
# def input(): return sys.stdin.readline().rstrip()
# sys.setrecursionlimit(10 ** 7)

N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]

def check(t, s):
    if t==s:   # 同じ
        return True
    elif len(t)==len(s)+1:   # 1文字挿入
        for i in range(len(s)):
            if t[i]!=s[i]:
                error_idx = i   # 挿入箇所
                break
        else:
            if t[-1].islower():  # 最後に挿入
                return True
            else:
                return False
        # 挿入文字が英子文字で、挿入箇所以降が同じ
        if t[error_idx].islower() and t[error_idx+1:]==s[error_idx:]:
            return True
    elif len(t)+1==len(s):   # 1文字削除
        for i in range(len(t)):
            if t[i]!=s[i]:
                error_idx = i   # 削除箇所
                break
        else:
            return True  # 最後を削除
        # 削除箇所以降が同じ
        if t[error_idx:]==s[error_idx+1:]:
            return True
    elif len(t)==len(s):   # 1文字置換
        for i in range(len(t)):
            if t[i]!=s[i]:
                error_idx = i
                break
        if t[error_idx].islower() and t[error_idx+1:]==s[error_idx+1:]:
            return True
    return False
        
ans = []
for i in range(N):
    if check(T, S[i]):
        ans.append(i+1)

print(len(ans))
print(*ans)
