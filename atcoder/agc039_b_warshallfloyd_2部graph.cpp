// https://atcoder.jp/contests/agc039/tasks/agc039_b
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
#include<queue>
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int n;
vector<vector<int>> g;
vector<int> color;

bool dfs(int v, int c) {   // 2部グラフ判定 頂点iの色(1 or -1)
    color[v] = c;   // 頂点vをcで塗る
    rep(i,n) if(g[v][i]==1) {
        if (color[i] == c) return false;                // 隣接している頂点が同じ色ならfalse
        if (color[i] == 0 && !dfs(i, -c)) return false; // 隣接している頂点がまだ塗られていないなら-cで塗る
    }
    return true;    // すべての頂点を塗れたらtrue
}

int main() {
    cin >> n;
    g = vector<vector<int>>(n,vector<int>(n, INF));
    rep(i,n) {
        string s;
        cin >> s;
        rep(j,n) {
            if (s[j] == '1') g[i][j] = 1;
            else if (i==j)   g[i][j] = 0;
        }
    }
    rep(k,n) rep(i,n) rep(j,n) {    // warshall_floyd
        g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
    }
    int ans = -1;
    rep(i,n) rep(j,n) ans = max(ans, g[i][j]+1);

    color = vector<int>(n);
    if (!dfs(0,1)) ans = -1;    // 2部グラフでなければ-1
	cout << ans << endl;
	return 0;
}
