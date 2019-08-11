// aribook238 DP 重複組み合わせ
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
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

const int MAX_N = 1000;
const int MAX_M = 1000;

// 入力
int n, m;
int MOD = 10000;
int a[MAX_N];
int dp[MAX_N + 1][MAX_M + 1];	// DPテーブル

int main() {
	cin >> n >> m;
	rep(i, n) {
		cin >> a[i];
	}

	// 動的計画法(DP)
	// 1つも選ばない方法は常に一通り
	rep(i, n + 1) {
		dp[i][0] = 1;
	}
	rep (i, n) {
		for (int j = 0;  j < m + 1; j++) {
			if (j - 1 - a[i] >= 0) {
				// 引き算が含まれる場合には負の数にならないように注意する
				dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a[i]] + MOD) % MOD;
			}
			else {
				dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % MOD;
			}
		}
	}

	cout << dp[n][m] << endl;

	return 0;
}
