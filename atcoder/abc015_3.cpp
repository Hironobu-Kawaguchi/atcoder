// https://atcoder.jp/contests/abc015/tasks/abc015_3
#include<iostream>
//#include<algorithm>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int N, K;
vector<vector<int>> T(5, vector<int>(5));

bool dfs(int numQ, int value) {	// numQ: 今の質問数
	if (numQ == N) return (value == 0);	// 質問がもうなければ、XORが0になっているかを調べる
	for (int i = 0; i < K; i++)
	{
		if (dfs(numQ + 1, value ^ T[numQ][i])) return true;	// dfs関数の中からdfs関数をもう一度呼び出す
	}
	return false;	// 探索した結果、XORが0になる組み合わせが無ければfalse
}

int main() {
	cin >> N >> K;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < K; j++)
		{
			cin >> T[i][j];
		}
	}

	if (dfs(0, 0)) cout << "Found" << endl;
	else cout << "Nothing" << endl;

	return 0;
}
