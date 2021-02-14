// https://atcoder.jp/contests/arc111/tasks/arc111_b
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

const int MAX_A = 400005;
vector<vector<int>> G(MAX_A);
vector<bool> done(MAX_A);
int nodes, edges;

void dfs(int now) {
    if (done[now]) return;
    done[now] = true;
    nodes++;
    for (int next: G[now]) {
        edges++;
        dfs(next);
    }
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    // rep(i,MAX_A) done[i] = false;
    set<int> colors;
    rep(i,n) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        colors.emplace(a); colors.emplace(b);
        G[a].push_back(b); G[b].push_back(a);
    }
    int ans = 0;
    for (int c: colors) {
        if (done[c]) continue;
        nodes = 0; edges = 0;
        dfs(c);
        if (nodes==(edges/2)+1) ans += nodes - 1;  // クラスタが木の場合はnode数-1
        else                    ans += nodes;      // クラスタが木以外の場合はnode数
    }
	cout << ans << "\n";
	return 0;
}
