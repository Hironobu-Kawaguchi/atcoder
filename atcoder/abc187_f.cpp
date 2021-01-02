// https://atcoder.jp/contests/abc187/tasks/abc187_f
// https://atcoder.jp/contests/abc187/submissions/19168007
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
    int n, m;
    cin >> n >> m;
    vector<int> a(m), b(m);
    vector<int> e(n);

    rep(i,m) {
        cin >> a[i] >> b[i];
        a[i]--; b[i]--;
        e[a[i]] |= 1 << b[i];
        e[b[i]] |= 1 << a[i];
    }
    vector<int> dp(1 << n, 99999);
    dp[0] = 0;
    for (int i = 1; i < (1<<n); i++) {
        rep(j, n) {
            if ((i & (1<<j))==0) continue;
            int target = i - (1<<j);
            if(dp[target] <= 1 && (e[j] & target) == target) {
                dp[i] = 1;
            }
            // 1つ調べれば十分なのでbreak
            break;
        }
    }
    rep(i, (1<<n)) {
        for (int j = i; j > 0; j = (j-1) & i) {
            // iをjとkの2つのグループに分ける。このi,jのループはO(3^n)
            int k = i-j;
            // 適切な分け方を探して最小値を更新する
            dp[i] = min(dp[i], dp[j] + dp[k]);
        }
    }
    cout << dp[(1 << n) - 1] << endl;
	return 0;
}
