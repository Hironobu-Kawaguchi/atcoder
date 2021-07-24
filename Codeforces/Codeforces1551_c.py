# http://codeforces.com/contest/1551/problem/C

from collections import Counter

def main():
    n = int(input())
    s = 'abcde'
    d = dict(zip(s, range(5)))
    # print(d)
    word_list = []
    for i in range(n):
        word = input().rstrip()
        word_list.append(word)
    # print(word_list)
    diff_list = [[] for _ in range(5)]
    for i in range(n):
        cnt = Counter(word_list[i])
        for j in range(5):
            diff_list[j].append(cnt[s[j]]*2 - len(word_list[i]))
    for j in range(5):
        diff_list[j].sort(reverse=True)
    # print(diff_list)
    ans = 0
    for j in range(5):
        count = 0
        tot = diff_list[j][0]
        while tot>0:
            count += 1
            if count>=n: break
            tot += diff_list[j][count]
        ans = max(ans, count)
    print(ans)
    return

t = int(input())
for i in range(t):
    main()
