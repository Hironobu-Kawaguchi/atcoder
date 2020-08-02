// https://atcoder.jp/contests/abc046/tasks/arc062_a
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;


int main() {
	// 入力
	int N;
	cin >> N;

	vector<ll> T(N), A(N);
	rep(i, N) {
		cin >> T[i] >> A[i];
	}
	ll tmp;
	for (int i = 1; i < N; i++)
	{
		tmp = max((T[i - 1] + T[i] - 1) / T[i], (A[i - 1] + A[i] - 1) / A[i]);
		T[i] *= tmp;
		A[i] *= tmp;
	}
	ll ans = T[N - 1] + A[N - 1];
	cout << ans << endl;

	return 0;
}
