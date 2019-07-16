//https://atcoder.jp/contests/abc132/tasks/abc132_e
//https://atcoder.jp/contests/abc132/submissions/6188357
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

const int INF = 1001001001;
vector<vector<int>> dist(100005, vector<int>(3, INF));

int main() {
	int n, m;
	cin >> n >> m;

	// 有向グラフG
	vector<vector<int>> to(n);
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		a--; b--;
		to[a].push_back(b);
	}

	int sv, tv;
	cin >> sv >> tv;
	sv--; tv--;

	// BFS（幅優先探索）
	queue<pair<int, int>> q;
	q.push(pair<int, int>(sv, 0));
	dist[sv][0] = 0;
	while (!q.empty()) {
		int v = q.front().first;
		int l = q.front().second;
		q.pop();
		for (int u : to[v]) {
			int nl = (l + 1) % 3;
			if (dist[u][nl] != INF) continue;
			dist[u][nl] = dist[v][l] + 1;
			q.push(pair<int, int>(u, nl));
		}
	}
	int ans = dist[tv][0];
	if (ans == INF) ans = -1;
	else ans /= 3;
	cout << ans << endl;
	return 0;
}
