// https://atcoder.jp/contests/abc125/tasks/abc125_c
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

long long gcd(long long x, long long y) {
	return y ? gcd(y, x % y) : x;
}

int main() {
	long long N;
	cin >> N;
	vector<long long> A(N), gcd_l(N+1, 0), gcd_r(N+1, 0), gcds(N);
	for (long long i = 0; i < N; i++)
	{
		cin >> A[i];
	}

	for (long long i = 0; i < N; i++)
	{
		gcd_l[i + 1] = gcd(gcd_l[i], A[i]);
		gcd_r[i + 1] = gcd(gcd_r[i], A[N - i - 1]);
	}

	long long ans = 0;
	for (long long i = 0; i < N; i++)
	{
		gcds[i] = gcd(gcd_l[i], gcd_r[N - i - 1]);
		ans = max(gcds[i], ans);
	}

	cout << ans << endl;
	return 0;
}
