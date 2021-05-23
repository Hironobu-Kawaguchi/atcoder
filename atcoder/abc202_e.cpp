// https://atcoder.jp/contests/abc202/tasks/abc202_e
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

const int MAX_V = 200005;
vector<int> to[MAX_V];
int dep[MAX_V];    // each node depth
int in[MAX_V];     // each node in order (Euler Tour)
int out[MAX_V];    // each node out order (Euler Tour)
int k;             // order number (Euler Tour)
vector<int> ls[MAX_V];   // each depth in order list

void dfs(int v, int d) {
    in[v] = k; k++;    // in order number (Euler Tour)
    dep[v] = d;        // depth
    for (int u: to[v]) dfs(u, d+1);
    out[v] = k;        // out order number (Euler Tour)
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
    rep(i,n-1) {
        int p;
        cin >> p;
        to[p-1].push_back(i+1);
    }
    dfs(0, 0);
    rep(i,n) ls[dep[i]].push_back(in[i]);       // each depth in order list
    rep(i,n) sort(ls[i].begin(), ls[i].end());  // sort for binary search

    int q;
    cin >> q;

    auto f = [&](int d, int r) {  // binary search
        return int(lower_bound(ls[d].begin(), ls[d].end(), r) - ls[d].begin());
    };
    rep(qi, q) {
        int u, d;
        cin >> u >> d;
        --u;
        int ans = f(d, out[u]) - f(d, in[u]);  // count nodes by binary search
        printf("%d\n", ans);
    }

	return 0;
}
