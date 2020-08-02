// https://atcoder.jp/contests/past201912-open/tasks/past201912_i
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
// #define chmin(x,y) x = min(x,y)
// #define chmax(x,y) x = max(x,y)
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
// ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
// ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int n, m;
	cin >> n >> m;
    vector<ll> dp(1<<n, LINF);
    dp[0] = 0;
    string s; int c;
    rep(i,m) {
        cin >> s >> c;
        ll k = 0;
        rep(i,n) if(s[i]=='Y') k |= (1 << (n-i-1));
        rep(j,(1<<n)) {
            chmin(dp[j | k], dp[j] + c);
        }
    }
    if (dp[(1<<n)-1] == LINF) {
        cout << -1 << endl;
    } else {
        cout << dp[(1<<n)-1] << endl;
    }
	return 0;
}
