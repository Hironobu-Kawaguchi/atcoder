// https://atcoder.jp/contests/abc148/tasks/abc148_f
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

vector<vector<int>> to(100005);
int n;
vector<int> dist;
void dfs(int v, int d=0, int p=-1) {
	dist[v] = d;
	for (int u : to[v]) {
		if (u == p) continue;
		dfs(u, d+1, v);
	}
}
vector<int> calcDist(int s) {
	dist = vector<int>(n);
	dfs(s);
	return dist;
}

int main() {
	cin >> n;
	int s, t;
	cin >> s >> t;
	--s; --t;
	rep(i,n-1) {
		int a, b;
		cin >> a >> b;
		--a; --b;
		to[a].push_back(b);
		to[b].push_back(a);
	}
	vector<int> distS = calcDist(s);
	vector<int> distT = calcDist(t);

    int mx = 0;
	rep(i,n) {
		if (distS[i] < distT[i]) {
			mx = max(mx, distT[i]);
		}
	}
	int ans = mx-1;
	cout << ans << endl;
	return 0;
}
