// 蟻本p.94　例題 2-5-1　二部グラフ判定
#include<iostream>
//#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

const int MAX_V = 1000;
vector<int> G[MAX_V];	// グラフ
int V, E;				// 頂点数, 辺数
int color[MAX_V];		// 頂点iの色 (1 or -1)

// 頂点を1と-1で塗っていく
bool dfs(int v, int c) {
	color[v] = c;	// 頂点vをcで塗る
	for (int i = 0; i < G[v].size(); i++)
	{
		// 隣接している頂点が同じ色ならfalse
		if (color[G[v][i]] == c) return false;
		// 隣接している頂点がまだ塗られていないなら-cで塗る
		if (color[G[v][i]] == 0 && !dfs(G[v][i], -c)) return false;
	}
	// 全ての頂点を塗れたらtrue
	return true;
}

int main() {
	cin >> V >> E;
	for (int i = 0; i < E; i++)
	{
		// sからtへの辺を張る
		int s, t;
		cin >> s >> t;
		G[s].push_back(t);
		G[t].push_back(s);	// 無向グラフなので、両方向の辺を張る
	}

	for (int i = 0; i < V; i++)
	{
		if (color[i] == 0)
		{
			// まだ頂点iが塗られていなければ1で塗る
			if (!dfs(i, 1)) {
				cout << "No" << endl;
				return 0;
			}
		}
	}

	cout << "Yes" << endl;
	return 0;
}
