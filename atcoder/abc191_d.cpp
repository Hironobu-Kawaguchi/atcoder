// https://atcoder.jp/contests/abc191/tasks/abc191_d
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

// 小数を10000倍して、小数計算の誤差を防ぐためroundする
int in() {
    double x;
    cin >> x;
    return round(x * 10000);
}

bool ok(ll dx, ll dy, ll r) {
    return dx*dx + dy*dy <= r*r;
}

ll f(ll x, ll y, ll z, ll lim) {
    int l = 0, r = 1;
    ll res = 0;
    for (int i = int(1e5)+5; i >= lim; i--) {
        while (ok(x-l*10000, i*10000-y, z)) --l;
        while (ok(r*10000-x, i*10000-y, z)) ++r;
        res += r-l-1;
    }
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    ll x = in();
    ll y = in();
    ll r = in();
    x %= 10000;  // [0,1)にしておく
    y %= 10000;  // [0,1)にしておく
    ll ans = f(x, y, r, 1);
    ans += f(x, -y, r, 0);
    cout << ans << "\n";
	return 0;
}
