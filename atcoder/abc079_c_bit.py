# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

s = input()

for bit in range(1 << 3):
    ans = int(s[0])
    f = s[0]

    for i in range(3):
        # フラグが立っていれば "+" 、なければ "-"
        if bit & (1 << i):
            ans += int(s[i + 1])
            f += "+"
        else:
            ans -= int(s[i + 1])
            f += "-"
        f += s[i + 1]

    if ans == 7:
        print(f + "=7")
        exit()
