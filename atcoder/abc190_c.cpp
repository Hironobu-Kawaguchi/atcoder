// https://atcoder.jp/contests/abc190/tasks/abc190_c
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
	int n, m, k;
	cin >> n >> m;
    vector<int> a(m), b(m);
    rep(i,m) {
        cin >> a[i] >> b[i];
        a[i]--; b[i]--;
    }
    cin >> k;
    vector<int> c(k), d(k);
    rep(i,k) {
        cin >> c[i] >> d[i];
        c[i]--; d[i]--;
    }
    int ans = 0;
    rep(bi, 1<<k) {
        vector<bool> dish(n);
        rep(i,k) {
            if ((bi>>i)&1) dish[c[i]] = true;
            else           dish[d[i]] = true;
        }
        int cnt = 0;
        rep(i,m) {
            if (dish[a[i]]==true & dish[b[i]]==true) cnt++;
        }
        ans = max(ans, cnt);
    }

	cout << ans << "\n";
	return 0;
}
