# https://atcoder.jp/contests/tenka1-2015-qualb/tasks/tenka1_2015_qualB_b


S = input()
ans = "set"
dim = 0
for c in S:
    if dim == 1:
        if c == ':':
            ans = "dict"
            break
        elif c == ',':
            break
    if c == '{':
        dim += 1
    elif c == '}':
        dim -= 1
if S == "{}":
    ans = "dict"
print(ans)
