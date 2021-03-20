// https://atcoder.jp/contests/abc196/tasks/abc196_c
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
	ll n;
	cin >> n;
    ll ans = 0;
    // for (int i = 1; i <= 5; i++) {   // WA
    for (int i = 1; i <= 6; i++) {
        ll start = 1;
        rep(k,i-1) start *= 10;
        for (ll j = start; j <= start*10-1; j++) {
            // cout << (ll)j*(1+pow(10,i)) << endl;
            ll x = (ll) j*start*10 + j;
            if (x<=n) ans++;
        }
    }
	cout << ans << "\n";
	return 0;
}

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	ll n;
// 	cin >> n;
//     ll ans = 0;
//     for (int i = 1; i <= 1000000; i++) {
//         ll x = stoll(to_string(i) + to_string(i));
//         if (x<=n) ans++;
//     }
// 	cout << ans << "\n";
// 	return 0;
// }
