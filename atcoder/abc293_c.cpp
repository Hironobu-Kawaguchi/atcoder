// https://atcoder.jp/contests/abc293/tasks/abc293_c
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include <ctime>
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
    int h, w;
	cin >> h >> w;
    vector a(h, vector<int>(w));
    rep(i,h)rep(j,w) cin >> a[i][j];
    set<int> s;
    int ans = 0;

    auto dfs = [&](auto f, int i, int j) -> void {
        if (i >= h || j >= w) return;
        if (s.count(a[i][j])) return;
        if (i == h-1 && j == w-1) { ans++; return;}
        s.insert(a[i][j]);
        f(f, i, j+1);
        f(f, i+1, j);
        s.erase(a[i][j]);
    };
    dfs(dfs, 0,0);
    cout << ans << endl;
	return 0;
}
