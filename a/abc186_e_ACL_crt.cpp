// https://atcoder.jp/contests/abc186/tasks/abc186_e
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

// {g,x,y}: ax+by=g
tuple<ll,ll,ll> extgcd(ll a, ll b) {
    if (b == 0) return {a,1,0};
    ll g, x, y;
    tie(g,x,y) = extgcd(b, a%b);
    return {g,y,x-a/b*y};
}

void solve() {
    ll n, s, k;
    cin >> n >> s >> k;
    pair<ll,ll> p = crt({0,s},{n,k});
    if (p.second == 0) {
        cout << -1 << endl;
        return;
    }
    ll y = p.first;
    if (y < s) y += p.second;
    ll ans = (y-s)/k;
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    rep(i,t) solve();
	return 0;
}
