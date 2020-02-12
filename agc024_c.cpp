// https://atcoder.jp/contests/agc024/tasks/agc024_c
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
#define all(v) (v).begin(),(v).end()
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
	int n;
	cin >> n;
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    ll ans = 0, pre = 0;
    for (int i = n-1; i >= 0; i--) {
        if (a[i] < pre - 1) {
            cout << -1 << endl;
            return 0;
        } else if (a[i] != pre - 1) {
            ans += a[i];
        }
        pre = a[i];
    }
    if (a[0] != 0) {
        cout << -1 << endl;
        return 0;
    }
	cout << ans << endl;
	return 0;
}
