// https://atcoder.jp/contests/abc180/tasks/abc180_e
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
    int n;
	cin >> n;
    vector<vector<int>> city(n, vector<int>(3));
    rep(i,n) {
        cin >> city[i][0] >> city[i][1] >> city[i][2];
    }
    vector<vector<int>> dist(n, vector<int>(n));
    rep(i,n) rep(j,n) {
        dist[i][j] = abs(city[j][0]-city[i][0]) + abs(city[j][1]-city[i][1]) + max(0, city[j][2]-city[i][2]);
    }
    int n2 = 1<<n;
    vector<vector<int>> dp(n2, vector<int>(n, INF));
    rep(i,n) {
        if(i==0) continue;
        dp[1<<i][i] = dist[0][i];
    }
    rep(i,n2) rep(j,n) {
        if (!(i>>j&1)) continue;
        rep(k,n) {
            if (i>>k&1) continue;
            chmin(dp[i|1<<k][k], dp[i][j] + dist[j][k]);
        }
    }
	cout << dp[n2-1][0] << "\n";
	return 0;
}



// const int MAX_N = 17;
// vector<vector<int>> to(MAX_N, vector<int>(MAX_N));
// int n;
// int ans = INF;

// void dfs(int from, int bit, int dist) {
//     // cout << bit << (1<<n)-1 << endl;
//     if (bit==((1<<n)-1)) {
//         ans = min(ans, dist+to[from][0]);
//         return;
//     }
//     // cout << bit << endl;
//     rep(i,n) if(!(bit>>i)&1) {
//         // cout << i << bit+(1<<i) << dist + to[from][i] << endl;
//         if(from==i) continue;
//         dfs(i, bit + (1<<i), dist + to[from][i]);
//     }
//     // if(from==0) return;
//     // dfs(0, bit, dist + to[from][0]);
//     return;
// }

// int main() {
//     // cin.tie(nullptr);
//     // ios::sync_with_stdio(false);
// 	cin >> n;
//     vector<vector<int>> city(n, vector<int>(3));
//     rep(i,n) {
//         cin >> city[i][0] >> city[i][1] >> city[i][2];
//     }
//     rep(i,n) rep(j,n) {
//         to[i][j] = abs(city[j][0]-city[i][0]) + abs(city[j][1]-city[i][1]) + max(0, city[j][2]-city[i][2]);
//     }
//     // cout << "check" << endl;
//     dfs(0, 1, 0);
// 	cout << ans << "\n";
// 	return 0;
// }
