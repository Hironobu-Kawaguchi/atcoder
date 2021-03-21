// 蟻本p.95　単一始点最短路問題1（ベルマンフォード法）
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
// #include<queue>
// #include<deque>
// #include<regex>
// #include<bitset>
// #include<iomanip>
// #include<complex>
// #include<stack>
// #include<functional>

#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MAX_V = 1000, MAX_E = 1000;
// 頂点fromから頂点toへのコストcostの辺
struct edge { int from, to, cost; };
edge es[MAX_E];         // 辺

int d[MAX_V];	        // 最短距離
int V, E;				// 頂点数, 辺数

// s番目の頂点から各頂点への最短距離を求める
void shortest_path(int s) {
    rep(i, V) d[i] = INF;
    d[s] = 0;
    while (true) {
        bool update = false;
        rep(i, E) {
            edge e = es[i];
            if (d[e.from] != INF && d[e.to] > d[e.from] + e.cost) {
                d[e.to] = d[e.from] + e.cost;
                update = true;
            }
        }
        if (!update) break;
    }
	return;
}

int main() {
	cin >> V >> E;
	for (int i = 0; i < E; i++)
	{
		// sからtへの辺を張る
		int s, t, c;
		cin >> s >> t >> c;
		es[i].from = s;
		es[i].to   = t;
		es[i].cost = c;
	}

    shortest_path(0);

	cout << d[V-1] << endl;
	return 0;
}
