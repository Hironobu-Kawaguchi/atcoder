// https://atcoder.jp/contests/abc174/tasks/abc174_f
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

// Binary Indexed Tree (Fenwick Tree)
// https://youtu.be/lyHk98daDJo?t=7960
template<typename T>
struct BIT {
  int n;
  vector<T> d;
  BIT(int n=0):n(n),d(n+1) {}
  void add(int i, T x=1) {
    for (i++; i <= n; i += i&-i) {
      d[i] += x;
    }
  }
  T sum(int i) {
    T x = 0;
    for (i++; i; i -= i&-i) {
      x += d[i];
    }
    return x;
  }
  T sum(int l, int r) {
    return sum(r-1) - sum(l-1);
  }
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, q;
	cin >> n >> q;
    vector<int> c(n);
    rep(i,n) cin >> c[i];
    vector<int> pi(n+1, -1);
    vector<vector<int>> ps(n);
    rep(i,n) {
        int l = pi[c[i]];
        if (l != -1) ps[l].push_back(i);
        pi[c[i]] = i;
    }

    vector<vector<P>> qs(n);
    rep(qi,q) {
        int l, r;
        cin >> l >> r;
        --l; --r;
        qs[l].emplace_back(r,qi);
    }

    vector<int> ans(q);
    BIT<int> d(n);
    for (int x = n-1; x >= 0; --x) {
        for (int y : ps[x]) d.add(y,1);
        for (P query : qs[x]) {
          int r = query.first, i = query.second;
          ans[i] = (r-x+1) - d.sum(r);
        }
    }    

    rep(i,q) cout << ans[i] << "\n";
	return 0;
}
