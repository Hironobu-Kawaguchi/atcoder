// https://atcoder.jp/contests/abc174/tasks/abc174_c
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
const ll MOD = 1e9+7;

ll mod_pow(ll n, ll p, ll mod=MOD) {
    if(p==0) return 1;
    ll res = mod_pow(n*n%mod, p/2, mod);
    if(p%2==1) res = res * n % mod;
    return res;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int k;
	cin >> k;
    if(k%2==0) {
        cout << -1 << "\n";
        return 0;
    }
    int ans = 0, now = 0;
    while (true) {
        now += mod_pow(10, ans, k) * 7;
        now %= k;
        ans++;
        if (now==0) break;
        if (ans>k) {
            cout << -1 << "\n";
            return 0;
        }
    }
    cout << ans << "\n";
	return 0;
}
