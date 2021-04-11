// https://atcoder.jp/contests/abc191/tasks/abc191_d
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

struct E {
    int to, co;
    E(int to=0, int co=0): to(to), co(co) {}
};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    vector<vector<E>> g(n);
    rep(i,m) {
        int a, b, c;
        cin >> a >> b >> c;
        --a; --b;
        g[a].emplace_back(b,c);
    }
    rep(sv,n) {
        vector<int> dist(n,INF);
        priority_queue<P, vector<P>, greater<P>> q;  // 小さい順のpiority_queueにする
        auto push = [&](int v, int d) {
            if (dist[v] <= d) return;
            dist[v] = d;
            q.emplace(d,v);
        };
        for (auto&& e : g[sv]) push(e.to, e.co);  // 最初の移動、スタートに戻る距離を見るので、スタートを0にしない
        while (!q.empty()) {
            auto [d,v] = q.top(); q.pop();
            if (dist[v] != d) continue;
            for (auto&& e : g[v]) {
                push(e.to, d + e.co);
            }
        }
        int ans = dist[sv];
        if (ans == INF) ans = -1;
        cout << ans << endl;
    }
    return 0;
}
