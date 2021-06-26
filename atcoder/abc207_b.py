# https://atcoder.jp/contests/ABC207/tasks/abc207_b

def main():
    a, b, c, d = map(int, input().split())
    if b>=c*d:
        print(-1)
        return
    ans = (a+c*d-b-1) // (c*d-b)
    print(ans)

main()
