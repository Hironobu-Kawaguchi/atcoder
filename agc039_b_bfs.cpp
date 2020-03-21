// https://atcoder.jp/contests/agc039/tasks/agc039_b
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
#include<queue>
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int n;
vector<vector<int>> to;

int bfs(int sv) {
    queue<int> q;
    vector<int> dist(n, INF);
    q.push(sv);
    dist[sv] = 0;
    int res = 0;
    while (q.size()) {
        int v = q.front(); q.pop();
        res = max(res, dist[v]+1);
        for (int u: to[v]) {
            if (dist[u] != INF) continue;
            dist[u] = dist[v] + 1;
            q.push(u);
        }
    }
    rep(i,n) {      // 2部グラフ判定
        for (int j : to[i]) {
            if (abs(dist[i]-dist[j]) != 1) return -1;
        }
    }
    return res;
}

int main() {
    cin >> n;
    to = vector<vector<int>>(n);
    rep(i,n) {
        string s;
        cin >> s;
        rep(j,n) {
            if(s[j]=='1') to[i].push_back(j);
        }
    }
    int ans = -1;
    rep(i,n) ans = max(ans, bfs(i));
	cout << ans << endl;
	return 0;
}
