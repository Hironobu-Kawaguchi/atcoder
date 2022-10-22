// https://atcoder.jp/contests/abc274/tasks/abc274_e
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

// Geometry
const double eps = 1e-9;
bool equal(double a, double b) { return abs(a-b) < eps;}
 
// Vector
// https://youtu.be/UWbGRhF3Ozw?t=9564
struct V {
  double x, y;
  V(double x=0, double y=0): x(x), y(y) {}
  V& operator+=(const V& v) { x += v.x; y += v.y; return *this;}
  V operator+(const V& v) const { return V(*this) += v;}
  V& operator-=(const V& v) { x -= v.x; y -= v.y; return *this;}
  V operator-(const V& v) const { return V(*this) -= v;}
  V& operator*=(double s) { x *= s; y *= s; return *this;}
  V operator*(double s) const { return V(*this) *= s;}
  V& operator/=(double s) { x /= s; y /= s; return *this;}
  V operator/(double s) const { return V(*this) /= s;}
  double dot(const V& v) const { return x*v.x + y*v.y;}
  double cross(const V& v) const { return x*v.y - v.x*y;}
  double norm2() const { return x*x + y*y;}
  double norm() const { return sqrt(norm2());}
  V rotate90() const { return V(y, -x);}
  int ort() const { // orthant
    if (abs(x) < eps && abs(y) < eps) return 0;
    if (y > 0) return x>0 ? 1 : 2;
    else return x>0 ? 4 : 3;
  }
  bool operator<(const V& v) const {
    int o = ort(), vo = v.ort();
    if (o != vo) return o < vo;
    return cross(v) > 0;
  }
};
istream& operator>>(istream& is, V& v) {
  is >> v.x >> v.y; return is;
}
ostream& operator<<(ostream& os, const V& v) {
  os<<"("<<v.x<<","<<v.y<<")"; return os;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    int w = n+m+1;
    vector<V> p(w);
    rep(i,w-1) cin >> p[i];
    int w2 = 1<<w;
    vector<double> sp(w2,1);
    rep(s,w2) {
        rep(i,m) if(s>>(n+i)&1) sp[s] /= 2;
    }

    vector dist(w, vector<double>(w));
    rep(i,w) rep(j,w) dist[i][j] = (p[i]-p[j]).norm();

    const double INF = 1e18;
    vector dp(w2, vector<double>(w,INF));
    dp[0][n+m] = 0;
    rep(s,w2) rep(v,w) {
        if (dp[s][v]==INF) continue;
        rep(u,w) if (~s>>u&1) {
            chmin(dp[s|1<<u][u], dp[s][v]+dist[v][u]*sp[s]);
        }
    }

    int t = (1<<n)-1 | (1<<(n+m));
    double ans = INF;
    rep(s,w2) if ((s&t)==t) chmin(ans, dp[s][n+m]);
    printf("%.10f\n", ans);

	return 0;
}
