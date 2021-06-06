// https://atcoder.jp/contests/ABC204/tasks/abc204_c
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

const int MAX_N = 2005;
vector<vector<int>> to(MAX_N);
vector<bool> done(MAX_N);

int dfs(int now) {
    if (done[now]) return 0;
    done[now] = true;
    int ret = 0;
    for (int next: to[now]) {
        if (done[next]) continue;
        ret += dfs(next) + 1;
        // cout << ' ' << next << endl;
    }
    return ret;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int n, m;
	cin >> n >> m;
    // cout << n << m << endl;
    rep(i,m) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        // cout << a << b << endl;
        to[a].push_back(b);
    }
    // rep(i,n) for (int j: to[i]) {
    //     cout << j << i << endl;
    // }
    
    int ans = 0;
    rep(i,n) {
        rep(j,n) done[j] = false;
        // cout << i << endl;
        ans += dfs(i) + 1;
    }
	cout << ans << "\n";
	return 0;
}
