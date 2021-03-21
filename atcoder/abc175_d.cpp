// https://atcoder.jp/contests/abc175/tasks/abc175_b
#include <iostream>
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
    int n, k;
	cin >> n >> k;
    vector<int> p(n), c(n);
    rep(i,n) {
        cin >> p[i]; 
        p[i]--;
    }
    rep(i,n) cin >> c[i];

    ll ans = -LINF;
    rep(si,n) {
        vector<int> dists;
        int now = si;
        ll cycle = 0;
        while (true) {
            now = p[now];
            dists.push_back(c[now]);
            cycle += c[now];
            if (now == si) break;
        }
        int sz = dists.size();
        ll tot = 0;
        rep(i,sz) {
            tot += dists[i];
            if(i+1>k) break;
            ll total = tot; 
            if(cycle>0)  total += ((k-(i+1))/sz)*cycle;
            ans = max(ans, total);
        }
    }
    cout << ans << "\n";
	return 0;
}

// WA
// #include<bits/stdc++.h>
// using namespace std;
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// #define drep(i,n) for(int i = (n-1); i >= 0; i--)
// #define all(v) (v).begin(),(v).end()
// #define maxs(x,y) (x = max(x,y))
// #define mins(x,y) (x = min(x,y))
// template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
// template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
// template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
// template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
// typedef pair<int, int> P;
// typedef long long ll;
// const int INF = 1001001001;
// const ll LINF = 1001002003004005006ll;
// const ll MOD = 1e9+7;

// const int MAXN = 5000;
// int n, k;
// vector<int> p(MAXN), c(MAXN);
// vector<vector<int>> to_cnt(MAXN, vector<int>(MAXN));
// vector<vector<ll>> to_dist(MAXN, vector<ll>(MAXN));
// ll ans = -LINF;

// ll dfs(int now, int cnt, ll dist) {
//     if (cnt==k) return dist;
//     if (to_cnt[now][now]!=0 && to_cnt[now][now]*2<=k-cnt) {   // サイクルに入る
//         int cycle = (k-cnt) / to_cnt[now][now] - 1;           // 途中をチェックするため、1回は回すため -1
//         if (cnt==0) return dfs(now, cnt + cycle * to_cnt[now][now], dist + cycle * to_dist[now][now]);
//         else return max(dist, dfs(now, cnt + cycle * to_cnt[now][now], dist + cycle * to_dist[now][now]));
//     }
//     int next = p[now];
//     // if (to_cnt[now][next]==0) {
//     //     to_cnt[now][next] = 1;
//     //     to_dist[now][next] = c[next];
//     // }
//     if (cnt==0) return dfs(next, cnt+1, dist+c[next]);
//     else return max(dfs(next, cnt+1, dist+c[next]), dist);
// }

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	cin >> n >> k;

//     rep(i,n) {
//         cin >> p[i];
//         --p[i];
//     }
//     rep(i,n) {
//         cin >> c[i];
//     }

//     rep(i,n) {
//         queue<tuple<int, int, ll>> Q;
//         vector<bool> visited(n);
//         Q.emplace(i, 0, 0);
//         while (!Q.empty()) {
//             int now, cnt;
//             ll dist;
//             tie(now, cnt, dist) = Q.front();
//             Q.pop();
//             if (now!=i && visited[now]) continue;
//             visited[now] = true;
//             to_cnt[i][now] = cnt;
//             to_dist[i][now] = dist;
//             int next = p[now];
//             Q.emplace(next, cnt+1, dist+c[next]);
//         }
//     }

//     // rep(i,n) rep(j,n) {
//     //     cout << i << ' ' << j << ' ' << to_cnt[i][j] << ' ' << to_dist[i][j] << endl;
//     // }

//     rep(i,n) {
//         ans = max(ans, dfs(i, 0, 0));
//     }
//     cout << ans << "\n";
// 	return 0;
// }
