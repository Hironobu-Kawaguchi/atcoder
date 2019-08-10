// aribook231 DP ナップサック問題
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

const int MAX_N = 100;
const int MAX_W = 10000;
// 入力
int n, W;
int w[MAX_N], v[MAX_N];
int dp[MAX_N + 1][MAX_W + 1];	// メモ化テーブル

int main() {
	cin >> n >> W;
	for (int i = 0; i < n; i++)	{
		cin >> w[i] >> v[i];
	}

	// 動的計画法(DP)
	for (int i = n - 1; i >= 0; i--)
	{
		for (int j = 0; j <= W; j++)
		{
			if (j < w[i])
			{
				dp[i][j] = dp[i + 1][j];
			}
			else
			{
				dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i]);
			}
		}
	}
	cout << dp[0][W] << endl;

	return 0;
}
