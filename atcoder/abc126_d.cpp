// https://atcoder.jp/contests/abc126/tasks/abc126_d
// https://youtu.be/26AWkQNRb-A
// 蟻本p.94　例題 2-5-1　二部グラフ判定
#include<iostream>
//#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;


int main() {
	int N;					// 頂点数
	cin >> N;
	vector<vector<int>> to(N), cost(N);		// グラフ

	for (int i = 0; i < N-1; i++)	{
		// sからtへの辺を張る
		int s, t, w;
		cin >> s >> t >> w;
		s--;
		t--;
		to[s].push_back(t);  cost[s].push_back(w);
		to[t].push_back(s);	 cost[t].push_back(w);  // 無向グラフなので、両方向の辺を張る
	}

	vector<int> ans(N, -1);		// 頂点の色 塗る前:-1, 白:0, 黒:1
	queue<int> q;

	ans[0] = 0;
	q.push(0);

	while (!q.empty())	{
		int v = q.front();
		q.pop();
		for (int i = 0; i < to[v].size(); i++)	{
			int u = to[v][i];
			int w = cost[v][i];
			if (ans[u] != -1)	continue;
			ans[u] = (ans[v] + w) % 2;
			q.push(u);
		}
	}

	for (int i = 0; i < N; i++)	{
		cout << ans[i] << endl;
	}

	return 0;
}
