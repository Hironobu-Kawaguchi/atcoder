// https://atcoder.jp/contests/acl1/tasks/acl1_b
#include<bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    ll n;
    cin >> n;
    ll ans = LINF;
    for (ll a = 1; a * a <= 2 * n; a++) {
        if ((2 * n) % a != 0) continue;
        ll b = 2 * n / a;
        pair<ll,ll> res;  // CRT(中国剰余定理)
        res = crt({0, -1}, {a, b});
        if (res.second) ans = min(ans, (res.first == 0) ? res.second : res.first);
        res = crt({0, -1}, {b, a});
        if (res.second) ans = min(ans, (res.first == 0) ? res.second : res.first);
    }
    cout << ans << "\n";
    return 0;
}
