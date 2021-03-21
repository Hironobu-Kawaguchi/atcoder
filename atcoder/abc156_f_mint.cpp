// https://atcoder.jp/contests/abc156/tasks/abc156_f
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int divceil(int a, int b) {
    return (a+b-1)/b;
}

int main() {
	ll k, q;
	cin >> k >> q;
    vector<int> d(k);
    rep(i,k) cin >> d[i];
    rep(qi,q) {
        int n, x, m;
        cin >> n >> x >> m;
        ll last = x, eq = 0;
        rep(i,k) {
            ll num = divceil(n-1-i,k);
            last += (d[i]%m) * num;
            if (d[i]%m == 0) eq += num;
        }
        ll ans = (n-1) - (last/m - x/m) - eq;
        cout << ans << endl;
    }
	return 0;
}
