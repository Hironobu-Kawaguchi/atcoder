// https://atcoder.jp/contests/zone2021/tasks/zone2021_e
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
    int r, c;
    cin >> r >> c;
    vector<vector<int>> a(r, vector<int>(c-1));
    vector<vector<int>> b(r-1, vector<int>(c));
    rep(i,r) rep(j,c-1) cin >> a[i][j];
    rep(i,r-1) rep(j,c) cin >> b[i][j];

    priority_queue<P, vector<P>, greater<P>> q;
    vector<int> dist(r*c*2, INF);
    auto push = [&](int i, int j, int k, int x) {
        int v = i*c*2 + j*2 + k;
        if (dist[v] <= x) return;
        dist[v] = x;
        q.emplace(x, v);
    };
    push(0,0,0,0);
    while (!q.empty()) {
        auto [x, v] = q.top(); q.pop();
        if (dist[v] != x) continue;
        int i = v/(c*2);
        int j = v/2%c;
        int k = v%2;
        if (k==0) {
            if (j+1 < c) push(i, j+1, k, x+a[i][j]);
            if (j-1 >=0) push(i, j-1, k, x+a[i][j-1]);
            if (i+1 < r) push(i+1, j, k, x+b[i][j]);
            push(i, j, 1, x+1);
        } else {
            if (i-1 >=0) push(i-1, j, k, x+1);
            push(i, j, 0, x);
        }
    }
    int ans = dist[(r*c-1)*2];
	cout << ans << endl;
	return 0;
}
