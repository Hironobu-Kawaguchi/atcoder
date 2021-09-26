# input_file = 'input.txt'
input_file = 'read/test_lsim_00.txt'
with open(input_file) as f:
    in_list = f.readlines()
in_list.pop(0)
for i in range(len(in_list)):
    in_list[i] = in_list[i].replace('-', '')
# print(in_list)

output_file = 'output.txt'
out_rp_list = []
with open(output_file) as f:
    out_list = f.readlines()
for i in range(len(in_list)):
    out_rp_list.append(out_list[i].replace('-', ''))

for i in range(len(in_list)):
    if in_list[i]!=out_rp_list[i]:
        print("error line", i+1, "\n", in_list[i], out_list[i])
# print("finish check", len(in_list), "lines")

d = {'-':0, 'A':1, 'C':2 ,'G':3, 'T':4}
cs = 0
for i in range(len(out_list[0])):
    cnt = [0] * 5
    for j in range(len(out_list)):
        if out_list[j][i] in d:
            cnt[d[out_list[j][i]]] += 1
    cnt.sort(reverse=True)
    cs += cnt[1]

if len(out_list)<=10:
    score = 200 - cs//5
    print("small", len(out_list), "lines: score =", score)
else:
    score = 700 - cs//10
    print("large", len(out_list), "lines: score =", score)
