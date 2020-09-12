// https://codeforces.com/contest/1398/problem/D
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

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int R, G, B;
	cin >> R >> G >> B;
    vector<int> r(R), g(G), b(B);
    rep(i,R) cin >> r[i];
    rep(i,G) cin >> g[i];
    rep(i,B) cin >> b[i];
    sort(r.rbegin(),r.rend());
    sort(g.rbegin(),g.rend());
    sort(b.rbegin(),b.rend());
    int ans = 0;
    int dp[R+1][G+1][B+1];
    rep(i,R+1) rep(j,G+1) rep(k,B+1) dp[i][j][k] = 0;
    rep(i,R+1) rep(j,G+1) rep(k,B+1) {
        if (i<R && j<G) maxs(dp[i+1][j+1][k], dp[i][j][k] + r[i]*g[j]);
        if (i<R && k<B) maxs(dp[i+1][j][k+1], dp[i][j][k] + r[i]*b[k]);
        if (k<B && j<G) maxs(dp[i][j+1][k+1], dp[i][j][k] + g[j]*b[k]);
        maxs(ans, dp[i][j][k]);
    }
    cout << ans << endl;
	return 0;
}
