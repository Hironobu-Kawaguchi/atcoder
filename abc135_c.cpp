// https://atcoder.jp/contests/abc135/tasks/abc135_c
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


int main() {
	int N;
	cin >> N;
	vector<long long> A(N+1), B(N);

	for (int i = 0; i < N+1; i++)	{
		cin >> A[i];
	}
	for (int i = 0; i < N; i++) {
		cin >> B[i];
	}

	long long ans = 0;

	for (int i = 0; i < N; i++) {
		if (B[i] > A[i])
		{
			ans += A[i];
			long long tmp = min(B[i] - A[i], A[i + 1]);
			ans += tmp;
			A[i + 1] -= tmp;
		}
		else
		{
			ans += B[i];
		}
	}

	cout << ans << endl;

	return 0;
}
