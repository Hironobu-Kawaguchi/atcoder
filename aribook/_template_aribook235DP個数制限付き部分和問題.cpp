// aribook235 DP 個数制限付き部分和問題
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
const int MAX_K = 100000;
// 入力
int n, K;
int a[MAX_N], m[MAX_N];	// a:値, m:個数
int dp[MAX_K + 1];	// DPテーブル

int main() {
	cin >> n >> K;
	for (int i = 0; i < n; i++) {
		cin >> a[i] >> m[i];
	}

	// 動的計画法(DP)
	memset(dp, -1, sizeof(dp));
	dp[0] = true;
	for (int i = 0; i < n; i++)	{
		for (int j = 0; j <= K; j++)		{
			if (dp[j] >= 0)			{
				dp[j] = m[i];
			}
			else if (j < a[i] || dp[j-a[i]] <= 0)	{
				dp[j] = -1;
			}
			else
			{
				dp[j] = dp[j - a[i]] - 1;
			}
		}
	}

	if (dp[K] >= 0)
	{
		cout << "Yes" << endl;
	}
	else
	{
		cout << "No" << endl;
	}

	return 0;
}
