# https://atcoder.jp/contests/abc166/tasks/abc166_f
# 1,1 の時は次の候補も見る

# import sys
# # def input(): return sys.stdin.readline().rstrip()
# # input = sys.stdin.readline
# input = sys.stdin.buffer.readline
# sys.setrecursionlimit(10 ** 7)

d = {'A':0, 'B':1, 'C':2}
ABC = 'ABC'

def main():
    N, A, B, C = map(int, input().split())
    abc_nums = [A, B, C]
    S = []
    for i in range(N):
        s = input()
        flgs = []
        for j in range(2):
            flgs.append(d[s[j]])
        S.append(flgs)

    ans = []
    for i in range(N):
        if abc_nums[S[i][0]] == abc_nums[S[i][1]] == 0:
            print('No')
            return
        elif i == N-1:  # 最後だったらどちらでも
            if abc_nums[S[i][0]] <= abc_nums[S[i][1]]:
                abc_nums[S[i][0]] += 1
                ans.append(ABC[S[i][0]])
                abc_nums[S[i][1]] -= 1
            else:
                abc_nums[S[i][0]] -= 1
                abc_nums[S[i][1]] += 1
                ans.append(ABC[S[i][1]])
        elif abc_nums[S[i][0]] == abc_nums[S[i][1]]:    # 同じだったら次に出てくる方
            if S[i][0] == S[i+1][0] or S[i][0] == S[i+1][1]:
                abc_nums[S[i][0]] += 1
                ans.append(ABC[S[i][0]])
                abc_nums[S[i][1]] -= 1
            else:
                abc_nums[S[i][0]] -= 1
                abc_nums[S[i][1]] += 1
                ans.append(ABC[S[i][1]])
        elif abc_nums[S[i][0]] <= abc_nums[S[i][1]]:
            abc_nums[S[i][0]] += 1
            ans.append(ABC[S[i][0]])
            abc_nums[S[i][1]] -= 1
        else:
            abc_nums[S[i][0]] -= 1
            abc_nums[S[i][1]] += 1
            ans.append(ABC[S[i][1]])
    print('Yes')
    for i in range(N):
        print(ans[i])
    return
main()
