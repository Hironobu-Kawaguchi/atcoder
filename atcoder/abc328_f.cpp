// https://atcoder.jp/contests/abc328/tasks/abc328_f

#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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

struct WeightedUnionFind {
    vector<int> p;
    vector<ll> dif;
    WeightedUnionFind(int n): p(n, -1) ,dif(n) {}
    int root (int a) {
        if (p[a] < 0) return a;
        int b = p[a];
        p[a] = root(p[a]);
        dif[a] += dif[b];
        return p[a];
    }
    bool merge(int a, int b, ll w) {    // a = b + w
        root(a); root(b);
        w = w + dif[a] - dif[b];
        a = root(a); b = root(b);
        if (a == b) return w == 0;
        if (-p[a] < -p[b]) swap(a, b), w = -w;
        p[a] += p[b];
        p[b] = a; dif[b] = w;
        return true;
    }
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, q;
	cin >> n >> q;
    vector<int> ans;
    WeightedUnionFind uf(n);
    rep(i,q) {
        int a, b, d;
        cin >> a >> b >> d;
        --a; --b;
        if (uf.merge(a, b, d)) ans.push_back(i+1);
    }

	rep(i, ans.size()) cout << ans[i] << ' ';
	return 0;
}
