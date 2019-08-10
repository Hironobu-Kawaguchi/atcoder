// aribook231 DP ナップサック問題
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

const int MAX_N = 100;
// 入力
int n, W;
int w[MAX_N], v[MAX_N];

// i番目以降の品物から重さの総和がj以下となるように選ぶ
int rec(int i, int j) {
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
	return res;
}

int main() {
	cin >> n >> W;
	for (int i = 0; i < n; i++)	{
		cin >> w[i] >> v[i];
	}

	cout << rec(0, W) << endl;

	return 0;
}
