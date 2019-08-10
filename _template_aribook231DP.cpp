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

// i番目以降の品物から重さの総和がj以下となるように選ぶ
int rec(int i, int j) {
	if (dp[i][j] >= 0)
	{
		// 既に調べたことがあるならばその結果を再利用
		return dp[i][j];
	}
	int res;
	if (i == n)	{
		// もう品物は残っていない
		res = 0;
	}
	else if (j < w[i])
	{
		// この品物は入らない
		res = rec(i + 1, j);
	}
	else
	{
		// 入れない場合と入れる場合を両方試す
		res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i]);
	}
	// 結果をテーブルに記録する
	return dp[i][j] = res;
}

int main() {
	cin >> n >> W;
	for (int i = 0; i < n; i++)	{
		cin >> w[i] >> v[i];
	}

	//// まだ調べていないことを表す-1でメモ化テーブルを初期化
	//memset(dp, -1, sizeof(dp));
	//cout << rec(0, W) << endl;

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
