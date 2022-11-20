// https://atcoder.jp/contests/abc278/tasks/abc278_e
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
#include<map>
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
    int H, W, N, h, w;
    cin >> H >> W >> N >> h >> w;
    vector a(H, vector<int>(W));
    rep(i,H) rep(j,W) cin >> a[i][j];

    vector ans(H-h+1, vector<int>(W-w+1));
    rep(si, H-h+1) {
        vector<int> cnt(N+1);
        int now = 0;
        auto add = [&](int i, int j, int val=1) {
            int x = a[i][j];
            if (cnt[x] == 0) now++;
            cnt[x] += val;
            if (cnt[x] == 0) now--;
        };
        auto del = [&](int i, int j) { add(i,j,-1);};
        rep(i,H) rep(j,W) add(i,j);
        rep(i,h) rep(j,w-1) del(si+i,j);
        rep(j,W-w+1) {
            rep(i,h) del(si+i, w-1+j);
            ans[si][j] = now;
            rep(i,h) add(si+i, j);
        }
    }
    rep(i,ans.size()) {
        rep(j,ans[i].size()) cout << ans[i][j] << ' ';
        cout << endl;
    }
	return 0;
}
