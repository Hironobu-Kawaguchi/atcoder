// https://atcoder.jp/contests/abc172/tasks/abc172_c
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
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> a(n), b(m);
    rep(i,n) cin >> a[i];
    rep(i,m) cin >> b[i];

    ll t = 0;
    rep(i,m) t += b[i];    // bの合計

    // 尺取法
    int j = m;    // bはmから減らしていく
    int ans = 0;
    rep(i, n+1) {    // aは0からnまで増やしていく
        if (i>0) t += a[i-1];   // i個までの累計になるように足す 0個は0
        while (j>0 && t>k) {    // t<=k または j==0 で抜ける
            --j;
            t -= b[j];
        }
        if (t>k) break;    // bが0番まで行っても　t>k の場合はだめ
        ans = max(ans, i+j);
    }
	cout << ans << "\n";
	return 0;
}
