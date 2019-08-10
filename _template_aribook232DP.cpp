// aribook232 DP 最長共通部分列問題
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

const int MAX_N = 1000;
const int MAX_M = 1000;
// 入力
int n, m;
char s[MAX_N], t[MAX_M];
int dp[MAX_N + 1][MAX_M + 1];	// DPテーブル

int main() {
	cin >> n >> m;
	cin >> s;
	cin >> t;

	// 動的計画法(DP)
	for (int i = 0; i < n; i++)	{
		for (int j = 0; j < m; j++)		{
			if (s[i] == t[j])			{
				dp[i + 1][j + 1] = dp[i][j] + 1;			}
			else			{
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]);
			}
		}
	}
	cout << dp[n][m] << endl;

	return 0;
}
