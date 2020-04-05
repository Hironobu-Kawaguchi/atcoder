#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

const int MAX_N = 200005;

// auto mod int
// https://youtu.be/L8grWxBlIZ4?t=9858
// https://youtu.be/ERZuLAxZffQ?t=4807 : optimize
// https://youtu.be/8uowVvQ_-Mo?t=1329 : division
const int mod = 1000000007;
struct mint {
  ll x; // typedef long long ll;
  mint(ll x=0):x((x%mod+mod)%mod){}
  mint operator-() const { return mint(-x);}
  mint& operator+=(const mint a) {
    if ((x += a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator-=(const mint a) {
    if ((x += mod-a.x) >= mod) x -= mod;
    return *this;
  }
  mint& operator*=(const mint a) { (x *= a.x) %= mod; return *this;}
  mint operator+(const mint a) const { return mint(*this) += a;}
  mint operator-(const mint a) const { return mint(*this) -= a;}
  mint operator*(const mint a) const { return mint(*this) *= a;}
  mint pow(ll t) const {
    if (!t) return 1;
    mint a = pow(t>>1);
    a *= a;
    if (t&1) a *= *this;
    return a;
  }

  // for prime mod
  mint inv() const { return pow(mod-2);}
  mint& operator/=(const mint a) { return *this *= a.inv();}
  mint operator/(const mint a) const { return mint(*this) /= a;}
};
istream& operator>>(istream& is, const mint& a) { return is >> a.x;}
ostream& operator<<(ostream& os, const mint& a) { return os << a.x;}
// combination mod prime
// https://www.youtube.com/watch?v=8uowVvQ_-Mo&feature=youtu.be&t=1619
struct combination {
  vector<mint> fact, ifact;
  combination(int n):fact(n+1),ifact(n+1) {
    assert(n < mod);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i-1]*i;
    ifact[n] = fact[n].inv();
    for (int i = n; i >= 1; --i) ifact[i-1] = ifact[i]*i;
  }
  mint operator()(int n, int k) {
    if (k < 0 || k > n) return 0;
    return fact[n]*ifact[k]*ifact[n-k];
  }
} comb(MAX_N);

vector<int> to[MAX_N];

struct DP {
  mint dp;
  int t;
  DP(mint dp=1, int t=0):dp(dp),t(t) {}
  DP& operator+=(const DP& a) {
    dp *= a.dp;
    dp *= comb(t+a.t, t);
    t += a.t;
    return *this;
  }
  DP operator-(const DP& a) const {
    DP res(*this);
    res.t -= a.t;
    res.dp /= comb(res.t+a.t, res.t);
    res.dp /= a.dp;
    return res;
  }
  DP addRoot() const {
    DP res(*this);
    res.t++;
    return res;
  }
};

DP dp[MAX_N];

void dfs(int v, int p=-1) {
  for (int u : to[v]) {
    if (u == p) continue;
    dfs(u,v);
    dp[v] += dp[u].addRoot();
  }
}
void bfs(int v, int p=-1) {
  for (int u : to[v]) {
    if (u == p) continue;
    DP d = dp[v] - dp[u].addRoot();
    dp[u] += d.addRoot();
    bfs(u,v);
  }
}

int main() {
  int n;
  cin >> n;
  rep(i,n-1) {
    int a, b;
    cin >> a >> b;
    --a; --b;
    to[a].push_back(b);
    to[b].push_back(a);
  }
  dfs(0);
  bfs(0);
  rep(i,n) {
    cout << dp[i].addRoot().dp << endl;
  }
  return 0;
}
