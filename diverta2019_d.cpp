// https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d
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
	long long N;
	cin >> N;
	long long ans = 0;
	long long mx = sqrt(N);

	for (long long x = 1; x < mx+1; x++)
	{
		if (N % x == 0 && N / x - 1 > x) ans += N / x - 1;
	}

	cout << ans << endl;
	return 0;
}
