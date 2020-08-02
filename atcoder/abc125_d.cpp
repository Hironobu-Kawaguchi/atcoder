// https://atcoder.jp/contests/abc125/tasks/abc125_d
#include<iostream>
#include<algorithm>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	long long N;
	cin >> N;
	vector<long long> A(N);
	long long ans = 0, sumA = 0, cnt_neg = 0, min_abs = 1'000'000'000;
	for (long long i = 0; i < N; i++)
	{
		cin >> A[i];
		if (A[i] < 0) {
			cnt_neg++;
			sumA -= A[i];
		}
		else sumA += A[i];
		min_abs = min(abs(A[i]), min_abs);
	}

	if (cnt_neg % 2 == 0)
	{
		ans = sumA;
	}
	else
	{
		ans = sumA - 2 * min_abs;
	}

	cout << ans << endl;
	return 0;
}
