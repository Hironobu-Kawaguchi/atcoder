# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
def main(t):
    n = input()
    ans1, ans2 = '', ''
    for x in n:
        x = int(x)
        if x == 4:
            ans1 += '1'
            ans2 += '3'
        else:
            ans1 += '0'
            ans2 += str(x)
    print("Case #{}: {} {}".format(t, ans1, ans2))
        


t = int(input())
for i in range(t):
    main(i+1)
