# https://atcoder.jp/contests/abc295/tasks/abc295_a

def main():
    N = int(input())
    W = list(input().split())
    # print(W)

    cand = ["and", "not", "that", "the", "you"]
    for w in W:
        if w in cand:
            print("Yes")
            return
    print("No")
    return

main()
