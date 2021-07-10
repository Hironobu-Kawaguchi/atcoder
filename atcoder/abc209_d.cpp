// https://atcoder.jp/contests/abc209/tasks/abc209_d
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

int MAX_N = 100100;
vector<vector<int>> G(MAX_N);
vector<int> color(MAX_N);

void dfs(int v, int c) {
    color[v] = c;
    for (int next: G[v]) {
        if (color[next]==0) {
            dfs(next, -c);
        }
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
    rep(i,n-1) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    rep(i,n) if (color[i]==0) {
        dfs(i, 1);
    }

    rep(i,q) {
        int c, d;
        cin >> c >> d;
        c--; d--;
        if (color[c]==color[d]) {
            cout << "Town" << endl;
        } else {
            cout << "Road" << endl;
        }
    }
	return 0;
}
