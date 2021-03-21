// aribook237 DP 分割数
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
int dp[MAX_M + 1][MAX_N + 1];	// DPテーブル

int main() {
	cin >> n >> m;

	// 動的計画法(DP)
	dp[0][0] = 1;
	for (int i = 1; i < m + 1; i++) {
		rep (j, n + 1) {
			if (j - i >= 0) {
				dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % MOD;
			}
			else {
				dp[i][j] = dp[i - 1][j];
			}
		}
	}

	cout << dp[m][n] << endl;

	return 0;
}
