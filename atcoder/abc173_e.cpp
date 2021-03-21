// https://atcoder.jp/contests/abc173/tasks/abc173_e
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
// const ll MOD = 1e9+7;

// auto mod int
// https://youtu.be/L8grWxBlIZ4?t=9858
// https://youtu.be/ERZuLAxZffQ?t=4807 : optimize
// https://youtu.be/8uowVvQ_-Mo?t=1329 : division
const int mod = 1000000007;
// const int mod = 998244353;
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
istream& operator>>(istream& is, mint& a) { return is >> a.x;}
ostream& operator<<(ostream& os, const mint& a) { return os << a.x;}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, k;
	cin >> n >> k;
    vector<int> a(n);
    vector<int> s, t;
    rep(i,n) {
        cin >> a[i];
        if (a[i]<0) t.push_back(a[i]);    // t; 負
        else s.push_back(a[i]);           // s; 0以上
    }
    int S = s.size();
    int T = t.size();
    bool ok;
    if (S>0) {
        if (n==k) ok = (T%2==0);    // 全て選択で負の数が奇数ならfalse（正にできない）
        else ok = true;
    } else {
        ok = (k%2==0);              // すべて負で奇数ならfalse（正にできない）
    }
    mint ans = 1;
    if (!ok) {
        sort(a.begin(), a.end(), [](int x, int y) {
             return abs(x) < abs(y);
        });
        rep(i,k) ans *= a[i];   // false（正にできない）場合、絶対値が小さいものからk個かける
    } else {
        sort(s.begin(), s.end());   // 後ろから取っていくので正は昇順
        sort(t.rbegin(), t.rend()); // 後ろから取っていくので負は降順
        if (k%2==1) {       // 奇数個なら1個は正を選ぶ
            ans *= s.back();
            s.pop_back();
        }
        vector<ll> p;       // 2個ずつかけた数を格納
        while (s.size() >= 2) {
            ll x = s.back(); s.pop_back();
            x *= s.back(); s.pop_back();
            p.push_back(x);
        }
        while (t.size() >= 2) {
            ll x = t.back(); t.pop_back();
            x *= t.back(); t.pop_back();
            p.push_back(x);     // 負を2回かけるのでxは正
        }
        sort(p.rbegin(), p.rend()); // 降順にk//2個見ていく
        rep(i,k/2) ans *= p[i];
    }
    cout << ans << "\n";
	return 0;
}
