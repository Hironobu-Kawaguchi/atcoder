// aribook234 DP ナップサック問題その2
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>
#define INF 100000000

// #include <bits/stdc++.h>
using namespace std;

const int MAX_N = 100;
const long long MAX_W = 1000000000;	// Wが大きいのでVに対する最小のWを求める
const int MAX_V = 100;
// 入力
int n, W;
int w[MAX_N], v[MAX_N];
int dp[MAX_N + 1][MAX_N * MAX_V + 1];	// DPテーブル

int main() {
	cin >> n >> W;
	for (int i = 0; i < n; i++) {
		cin >> w[i] >> v[i];
	}

	// 動的計画法(DP)
	fill(dp[0], dp[0] + MAX_N * MAX_V + 1, INF);
	dp[0][0] = 0;
	for (int i = 0; i < n; i++)	{
		for (int j = 0; j <= MAX_N * MAX_V; j++)		{
			if (j < v[i])			{
				dp[i + 1][j] = dp[i][j];
			}
			else			{
				dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i]);
			}
		}
	}

	int res = 0;
	for (int i = 0; i <= MAX_N * MAX_V; i++)
	{
		if (dp[n][i] <= W)
		{
			res = i;
		}
	}
	cout << res << endl;

	return 0;
}
