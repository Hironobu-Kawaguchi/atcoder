// https://atcoder.jp/contests/abc054/tasks/abc054_c
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

const int MAX_N = 8;
bool G[MAX_N][MAX_N];

int dfs(int v, int N, bool visited[MAX_N]) {
    bool all_visited = true;
    rep(i,N) if(visited[i]==false) all_visited = false;
    if(all_visited) return 1;

    int ret = 0;
    rep(i,N) {
        if(G[v][i]==false) continue;
        if(visited[i]) continue;
        visited[i] = true;
        ret += dfs(i,N,visited);
        visited[i] = false;
    }
    return ret;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    rep(i,m) {
        int a, b;
        cin >> a >> b;
        G[a-1][b-1] = G[b-1][a-1] = true;
    }
    bool visited[MAX_N];
    rep(i,MAX_N) visited[i] = false;
    visited[0] = true;
	cout << dfs(0,n,visited) << "\n";
	return 0;
}
