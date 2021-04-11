// https://atcoder.jp/contests/abc198/tasks/abc198_b
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
// #include <atcoder/all>
// using namespace atcoder;
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

const int MAX_N = 1e5+5;
int n;
vector<int> c(MAX_N);
vector<vector<int>> G(MAX_N);
vector<int> Cs(MAX_N);
vector<int> visited(MAX_N), good(MAX_N);

void dfs(int now) {
	if (visited[now]) return;
	visited[now] = true;
	for (int next: G[now]){
		if (visited[next]) continue;
		if (Cs[c[next]]==0) good[next] = true;
		Cs[c[next]]++;
		dfs(next);
		Cs[c[next]]--;
	}	
	return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> n;
	rep(i,n) cin >> c[i];
	rep(i,n-1) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		G[a].push_back(b);
		G[b].push_back(a);
	}
	Cs[c[0]]++;
	good[0] = true;
	dfs(0);
	rep(i,n) {
		if(good[i]) cout << i+1 << "\n";
	}
	return 0;
}



// const int MAX_N = 1e5+5;
// int n;
// vector<int> c(MAX_N);
// vector<vector<int>> G(MAX_N);
// vector<set<int>> Cs(MAX_N);
// vector<int> visited(MAX_N), good(MAX_N);

// void dfs(int now) {
// 	if (visited[now]) return;
// 	visited[now] = true;
// 	for (int next: G[now]){
// 		if (visited[next]) continue;
// 		if (Cs[now].count(c[next])==0) good[next] = true;
// 		Cs[next] = Cs[now];
// 		Cs[next].insert(c[next]);
// 		dfs(next);
// 	}	
// 	return;
// }

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	cin >> n;
// 	rep(i,n) cin >> c[i];
// 	rep(i,n-1) {
// 		int a, b;
// 		cin >> a >> b;
// 		a--; b--;
// 		G[a].push_back(b);
// 		G[b].push_back(a);
// 	}
// 	Cs[0].insert(c[0]);
// 	good[0] = true;
// 	dfs(0);
// 	rep(i,n) {
// 		if(good[i]) cout << i+1 << "\n";
// 	}
// 	return 0;
// }
