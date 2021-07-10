// https://codeforces.com/contest/1542/problem/B
// https://codeforces.com/blog/entry/92492
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

void solve() {
    ll n, a, b;
    cin >> n >> a >> b;
    if (a==1) {
        if ((n-1)%b==0)	cout << "Yes" << "\n";
        else            cout << "No" << "\n";
    } else {
        ll now = 1;
        bool ok = false;
        while (now<=n) {
            if (now%b==n%b) {
                ok = true;
                break;
            }
            now *= a;
        }
        if (ok)	cout << "Yes" << "\n";
        else    cout << "No" << "\n";
    }
    return;
}

int main() {
    // cin.tie(nullptr);
    // ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) {
        solve();
    }
	return 0;
}
