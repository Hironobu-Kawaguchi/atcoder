# https://atcoder.jp/contests/arc105/tasks/arc105_a

def main():
    abcd = list(map(int, (input().split())))
    for i in range(1<<4):
        x, y = 0, 0
        for j in range(4):
            if (i>>j)&1:
                x += abcd[j]
            else:
                y += abcd[j]
        if x==y:
            print("Yes")
            return
    print("No")
    return
    
main()
