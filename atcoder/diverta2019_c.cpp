// https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<tuple>
#include<queue>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	int cntA = 0, cntB = 0, cntsame = 0;
	long long ans = 0;

	for (int i = 0; i < N; i++)
	{
		string tmp;
		cin >> tmp;
		int len = tmp.size();
		if (tmp[0] == 'B') cntB++;
		if (tmp[len - 1] == 'A') cntA++;
		if (tmp[0] == 'B' && tmp[len - 1] == 'A') cntsame++;
		for (int j = 0; j < len - 1; j++)
		{
			if (tmp[j] == 'A' && tmp[j + 1] == 'B') ans++;
		}
	}

	ans += min(cntA, cntB);
	if (cntA == cntB && cntA == cntsame && cntsame > 0) ans--;

	cout << ans << endl;
	return 0;
}
