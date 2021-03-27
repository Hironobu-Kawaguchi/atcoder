// https://atcoder.jp/contests/abc197/tasks/abc197_c
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n;
	cin >> n;
	vector<ll> a(n);
    rep(i,n) cin >> a[i];
    ll ans = LINF;
    rep(bi,1<<(n-1)) {
        ll now = a[0];
        vector<ll> ors;
        rep(i,n-1) {
            if (bi>>i&1) {
                now |= a[i+1];
            } else {
                ors.push_back(now);
                now = a[i+1];
            }
        }
        ors.push_back(now);
        // for (ll x: ors) cout << x;
        now = ors[0];
        rep(i,ors.size()-1) now ^= ors[i+1];
        // cout << now << ' ' << bi << ' ' << ors.size() << endl;
        ans = min(ans, now);
    }

	cout << ans << "\n";
	return 0;
}
