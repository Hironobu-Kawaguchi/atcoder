// aribook236 DP 最長増加部分列問題(LIS: Longest Increasing Subsequence)
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
// 入力
int n;
int a[MAX_N];
int dp[MAX_N];	// DPテーブル

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	// 動的計画法(DP)
	int res = 0;
	for (int i = 0; i < n; i++)	{
		dp[i] = 1;
		for (int j = 0; j < i; j++)		{
			if (a[j] > a[i])			{
				dp[i] = max(dp[i], dp[j] + 1);
			}
		}
		res = max(res, dp[i]);
	}

	cout << res << endl;

	return 0;
}
