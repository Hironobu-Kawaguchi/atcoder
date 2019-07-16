// https://atcoder.jp/contests/abc107/tasks/arc101_a
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
	int N, K;
	cin >> N >> K;

	vector<long long> x(N);

	for (int i = 0; i < N; i++)
	{
		cin >> x[i];
	}

	long long ans = 300'000'000;

	for (int i = 0; i < N - K + 1; i++)
	{
		long long pos = 0, neg = 0;
		if (x[i] < 0)     neg = -1 * x[i];
		if (x[i + K - 1] > 0) pos = x[i + K - 1];
		long long tmp = neg + pos + min(neg, pos);
		ans = min(tmp, ans);
	}

	cout << ans << endl;
	return 0;
}
