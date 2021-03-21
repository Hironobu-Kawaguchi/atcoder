// https://atcoder.jp/contests/abc139/tasks/abc139_e
// 有向グラフの最長経路問題に置き換えた解法
// DAG: ループなし
// トポロジカルソート

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
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

const int MAXN = 1005;
const int MAXV = MAXN*(MAXN-1)/2;
vector<int> to[MAXV];   // 頂点間の辺の情報
int id[MAXN][MAXN];     // 試合のid=DAGの頂点番号

int toId(int i, int j) {    // 選手idから試合idを返す関数
	if (i > j) swap(i,j);   // i,jが逆になっても試合idは同じ
	return id[i][j];
}

bool visited[MAXV];     // 訪問済み
bool calculated[MAXV];  // 計算済み
int dp[MAXV]; // max length of path from v   Vからスタートしたときの最長経路。頂点の個数ベースで経路の長さを数えるので、初期値は1

int dfs(int v) {
	if (visited[v]) {
		if (!calculated[v]) return -1;  // 計算が終わっていない頂点を2度訪れるのはループがあるということ
		return dp[v];
	}
	visited[v] = true;
	dp[v] = 1;
	for (int u : to[v]) {   // 全ての辺をなめる
		int res = dfs(u);
		if (res == -1) return -1;   // ループがあれば-1を返す
		dp[v] = max(dp[v], res+1);  // メモ化再帰っぽいこと(トポロジカルソートが同時にできる)
	}
	calculated[v] = true;
	return dp[v];
}

int main() {
	int n;
	cin >> n;
	vector<vector<int>> a(n, vector<int>(n-1));
	rep(i,n) {
		rep(j,n-1) {
			cin >> a[i][j];
			a[i][j]--;  // 選手idを0始まりに変換
		}
	}
	int V = 0;
	rep(i,n)rep(j,n) {
		if (i < j) {
			id[i][j] = V++; // 0から順に各試合にidを割り振る
		}
	}
	rep(i,n) {
		rep(j,n-1) {
			a[i][j] = toId(i,a[i][j]);  // 選手idを試合id(頂点番号)に置き換える
		}
		rep(j,n-2) {    // 頂点間の依存関係はn-2個
			to[a[i][j+1]].push_back(a[i][j]);
		}
	}
	int ans = 0;
	rep(i,V) {
		int res = dfs(i);
		if (res == -1) {
			cout << -1 << endl;     // ループがあれば-1を返す（問題文の指示）
			return 0;
		}
		ans = max(ans, res);
	}
	cout << ans << endl;
	return 0;
}
