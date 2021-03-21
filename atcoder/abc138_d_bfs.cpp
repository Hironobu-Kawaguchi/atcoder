// https://atcoder.jp/contests/abc138/tasks/abc138_d
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
	vector<vector<int>> edge(n);
	rep(i,n-1) {
		int a, b;
		cin >> a >> b;
		--a, --b;
		edge[a].push_back(b);
		edge[b].push_back(a);
	}
	vector<int> cnt(n);
	rep(i,q) {
		int p, x;
		cin >> p >> x;
		--p;
		cnt[p] += x;
	}
	queue<P> Q;
	vector<bool> visited(n);
	Q.emplace(0, -1);
	while(!Q.empty()) {
		P now;
		now = Q.front();
		Q.pop();
		if (visited[now.first]) continue;
		visited[now.first] = true;
		if (now.second!=-1) cnt[now.first] += cnt[now.second];
		for (int next: edge[now.first]) {
			Q.emplace(next, now.first);
		}	
	}
	rep(i,n) cout << cnt[i] << ' ';
	cout << "\n";
	return 0;
}
