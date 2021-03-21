// https://atcoder.jp/contests/abc188/tasks/abc188_f
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

ll x, y, ans = LINF;

void dfs(ll now, ll cnt) {
    // cout << ans << ' ' << x  << ' ' << now << ' ' <<  cnt << endl;
    if (now==x) {
        ans = min(ans, cnt);
        return;
    }
    ans = min(ans, cnt + abs(now - x));
    if (now%2) {
        ans = min(ans, cnt + 2 + abs((now+1)/2 - x));
    } else {
        ans = min(ans, cnt + 1 + abs(now/2 - x));
    }
    if (ans<=cnt) return;
    if (x>=now) {
        ans = min(ans, cnt + (x - now));
        return;
    }
    if (now%2) {
        dfs(now + 1, cnt + 1);
        dfs(now - 1, cnt + 1);
    } else {
        dfs(now / 2, cnt + 1);
    }
    return;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    cin >> x >> y;
    if (x>=y) {
        cout << x-y << endl;
        return 0;
    }
    // cout << ans << endl;
    dfs(y, 0);
    cout << ans << endl;
	return 0;
}