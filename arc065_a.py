# https://atcoder.jp/contests/abc049/tasks/arc065_a

def chk(S):
    n = len(S)
    i = n
    while i > 0:
        if S[i-5:i] == 'dream' or S[i-5:i] == 'erase':
            i -= 5
        elif S[i-6:i] == 'eraser':
            i -= 6
        elif S[i-7:i] == 'dreamer':
            i -= 7
        else:
            return False
    return True

S = input()
if chk(S):
    print("YES")
else:
    print("NO")
    