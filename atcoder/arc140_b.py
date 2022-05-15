# https://atcoder.jp/contests/arc140/tasks/arc140_b

N = int(input())
S = input()
cnts = []
cnt_a, cnt_r, cnt_c = 0, 0, 0
for i in range(len(S)):
    if S[i]=='C':
        if cnt_r==1:
            cnt_c += 1
        else:
            cnt_a, cnt_r, cnt_c = 0, 0, 0
    else:
        if cnt_r==1 and cnt_a>0 and cnt_c>0:
            cnts.append(min(cnt_a, cnt_c))
            cnt_a, cnt_r, cnt_c = 0, 0, 0
        if S[i]=='A':
            if i>0 and S[i-1]!='A':
                cnt_a = 1
            else:
                cnt_a += 1
            cnt_r, cnt_c = 0, 0
        else: # R
            cnt_r += 1
            cnt_c = 0
if cnt_r==1 and cnt_a>0 and cnt_c>0:
    cnts.append(min(cnt_a, cnt_c))
# print(cnts)
# print(sum(cnts))

sum_cnt = 0
can_even = 0
have_to_odd = []
for cnt in cnts:
    sum_cnt += cnt
    if cnt==1: can_even += 1
    if cnt>1: have_to_odd.append(cnt-1)
have_to_odd.sort(reverse=True)
ans = 0
while True:
    if ans%2==0: # odd
        if len(have_to_odd)==0:
            if can_even>0:
                can_even -= 1
            else:
                break
        elif have_to_odd[-1]==1:
            have_to_odd.pop()
            can_even += 1
        else:
            have_to_odd[-1] -= 1
    else: # even
        if can_even>0:
            can_even -= 1
        elif len(have_to_odd)>0: # もう使えなくなる
            have_to_odd.pop()
        else:
            break
    ans += 1

print(ans)
