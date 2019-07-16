// https://atcoder.jp/contests/abc127/tasks/abc127_c
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	int L, R;
	int left = 1, right = N;
	for (int i = 0; i < M; i++)
	{

		cin >> L >> R;
		left = max(L, left);
		right = min(R, right);
	}

	int ans = max(right - left + 1, 0);

	cout << ans << endl;

	return 0;
}
