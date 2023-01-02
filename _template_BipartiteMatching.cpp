// https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bq
#include <atcoder/maxflow>
#include <iostream>

using namespace std;
using namespace atcoder;

int main() {
	int N; char c[159][159];
	// 入力
	cin >> N;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) cin >> c[i][j];
	}

	// グラフを構成する
    mf_graph<int> Z(2 * N + 2 + 1);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (c[i][j] == '#') Z.add_edge(i, N + j, 1);
		}
	}
	for (int i = 1; i <= N; i++) {
		Z.add_edge(2 * N + 1, i, 1); // 「s → 青色」の辺
		Z.add_edge(N + i, 2 * N + 2, 1); // 「赤色 → t」の辺
	}
	// 答えの出力
	cout << Z.flow(2 * N + 1, 2 * N + 2) << endl;
	return 0;
}


// // https://github.com/E869120/kyopro-tessoku
// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// struct Edge {
// 	int to, cap, rev;
// };

// class MaximumFlow {
// public:
// 	int size_ = 0;
// 	bool used[409];
// 	vector<Edge> G[409];

// 	// 頂点数 N の残余グラフを準備
// 	void init(int N) {
// 		size_ = N;
// 		for (int i = 0; i <= size_; i++) G[i].clear();
// 	}

// 	// 頂点 a から b に向かう、上限 c リットル／秒の辺を追加
// 	void add_edge(int a, int b, int c) {
// 		int Current_Ga = G[a].size(); // 現時点での G[a] の要素数
// 		int Current_Gb = G[b].size(); // 現時点での G[b] の要素数
// 		G[a].push_back(Edge{ b, c, Current_Gb });
// 		G[b].push_back(Edge{ a, 0, Current_Ga });
// 	}

// 	// 深さ優先探索（F はスタートから pos に到達する過程での " 残余グラフの辺の容量 " の最小値）
// 	// 返り値は流したフローの量（流せない場合は 0 を返す）
// 	int dfs(int pos, int goal, int F) {
// 		// ゴールに到着：フローを流せる！
// 		if (pos == goal) return F;
// 		used[pos] = true;

// 		// 探索する
// 		for (int i = 0; i < G[pos].size(); i++) {
// 			// 容量 0 の辺は使えない
// 			if (G[pos][i].cap == 0) continue;

// 			// 既に訪問した頂点に行っても意味がない
// 			if (used[G[pos][i].to] == true) continue;

// 			// 目的地までのパスを探す
// 			int flow = dfs(G[pos][i].to, goal, min(F, G[pos][i].cap));

// 			// フローを流せる場合、残余グラフの容量を flow だけ増減させる
// 			if (flow >= 1) {
// 				G[pos][i].cap -= flow;
// 				G[G[pos][i].to][G[pos][i].rev].cap += flow;
// 				return flow;
// 			}
// 		}

// 		// すべての辺を探索しても見つからなかった ･･･
// 		return 0;
// 	}

// 	// 頂点 s から頂点 t までの最大フローの総流量を返す
// 	int max_flow(int s, int t) {
// 		int Total_Flow = 0;
// 		while (true) {
// 			for (int i = 0; i <= size_; i++) used[i] = false;
// 			int F = dfs(s, t, 1000000000);

// 			// フローを流せなくなったら操作終了
// 			if (F == 0) break;
// 			Total_Flow += F;
// 		}
// 		return Total_Flow;
// 	}
// };


// int N; char c[159][159];
// MaximumFlow Z; // MaximumFlow クラスは 9.8 節参照

// int main() {
// 	// 入力
// 	cin >> N;
// 	for (int i = 1; i <= N; i++) {
// 		for (int j = 1; j <= N; j++) cin >> c[i][j];
// 	}

// 	// グラフを構成する
// 	Z.init(2 * N + 2);
// 	for (int i = 1; i <= N; i++) {
// 		for (int j = 1; j <= N; j++) {
// 			if (c[i][j] == '#') Z.add_edge(i, N + j, 1);
// 		}
// 	}
// 	for (int i = 1; i <= N; i++) {
// 		Z.add_edge(2 * N + 1, i, 1); // 「s → 青色」の辺
// 		Z.add_edge(N + i, 2 * N + 2, 1); // 「赤色 → t」の辺
// 	}
// 	// 答えの出力
// 	cout << Z.max_flow(2 * N + 1, 2 * N + 2) << endl;
// 	return 0;
// }
