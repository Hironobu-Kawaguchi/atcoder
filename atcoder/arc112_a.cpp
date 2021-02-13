// https://atcoder.jp/contests/arc112/tasks/arc112_a
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

int solve() {
	int L, R;
	cin >> L >> R;
    ll ans = 0;
    if (2*L>R) {
        cout << 0 << "\n";
        return 0;
    }
    // for (int A = 2*L; A <= R; A++) {
    //     ans += min(A-L, R) - max(A-R, L) + 1;
    // }
    ll diff = R-2*L+1;
    ans += diff*(diff+1)/2;
	cout << ans << "\n";
	return 0;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int t;
	cin >> t;
    rep(i,t) solve();
	return 0;
}
