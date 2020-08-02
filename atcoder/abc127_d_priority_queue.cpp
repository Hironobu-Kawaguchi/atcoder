// https://atcoder.jp/contests/abc127/tasks/abc127_d
// https://youtu.be/SS6kW-d-rJ0 解説動画の解法
// A*1枚 と C*B枚 全てから上位N枚の合計を出せばよい（2回以上の入れ替えば無駄）
#include<iostream>
// #include<algorithm>
//#include <numeric>
//#include<string>
// #include<vector>
//#include<map>
//#include<tuple>
#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	priority_queue<pair<int, int>> q;

	for (int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		q.push(make_pair(a, 1));	// Aのカードは各1枚ずつ
	}

	for (int i = 0; i < M; i++) {
		int b, c;
		cin >> b >> c;
		q.push(make_pair(c, b));	// CのカードをB枚追加
	}

	long long ans = 0;

	for (int i = 0; i < N; i++)
	{
		pair<int, int> p = q.top();
		q.pop();
		ans += p.first;
		if (p.second > 1)
		{
			p.second--;
			q.push(p);
		}
	}

	cout << ans << endl;
	return 0;
}
