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
    int R, G, B, tmp;
	cin >> R >> G >> B;
    priority_queue<int> r, g, b;
    rep(i,R) {
        cin >> tmp;
        r.push(tmp);
    }
    rep(i,G) {
        cin >> tmp;
        g.push(tmp);
    }
    rep(i,B) {
        cin >> tmp;
        b.push(tmp);
    }
    ll ans = 0;
    int zero_cnt = 0, r_top = 0, g_top = 0, b_top = 0;
    if(r.empty()) zero_cnt++;
    if(g.empty()) zero_cnt++;
    if(b.empty()) zero_cnt++;
    // cout << zero_cnt << r.size() << g.size() << b.size() << ans << endl;
    while(zero_cnt<2) {
        if(!r.empty()) r_top = r.top();
        if(!g.empty()) g_top = g.top();
        if(!b.empty()) b_top = b.top();
        // cout << zero_cnt << r_top << g_top << b_top << ans << endl;
        if(r_top>=b_top && g_top>=b_top) {
            ans += r_top * g_top;
            r.pop(); g.pop();
        } else if(r_top>=g_top && b_top>=g_top) {
            ans += r_top * b_top;
            r.pop(); b.pop();
        } else if(g_top>=r_top && b_top>=r_top) {
            ans += g_top * b_top;
            g.pop(); b.pop();
            // cout << zero_cnt << r_top << g_top << b_top << ans << endl;
            // cout << zero_cnt << r.top() << g.top() << b.top() << ans << endl;
            // cout << zero_cnt << r.size() << g.size() << b.size() << ans << endl;
        }
        int zero_cnt = 0, r_top = 0, g_top = 0, b_top = 0;
        if(r.empty()) zero_cnt++;
        if(g.empty()) zero_cnt++;
        if(b.empty()) zero_cnt++;
        // cout << zero_cnt << r.top() << g.top() << b.top() << ans << endl;
    }
    cout << ans << endl;
	return 0;
}

// const int MAXN = 200;
// int R, G, B;
// vector<int> r(MAXN), g(MAXN), b(MAXN);
// ll ans = 0;

// void dfs(ll now, int ri, int gi, int bi) {
//     ll zero_cnt = 0;
//     if(ri==R) zero_cnt++;
//     if(gi==G) zero_cnt++;
//     if(bi==B) zero_cnt++;
//     if(zero_cnt>=2) {
//          ans = max(ans, now);
//          return;
//     }
//     if(ri!=R && gi!=G) dfs(now + r[ri]*g[gi], ri+1, gi+1, bi);
//     if(gi!=G && bi!=B) dfs(now + g[gi]*b[bi], ri, gi+1, bi+1);
//     if(bi!=B && ri!=R) dfs(now + b[bi]*r[ri], ri+1, gi, bi+1);
// }

// int main() {
//     cin.tie(nullptr);
//     ios::sync_with_stdio(false);
// 	cin >> R >> G >> B;
//     rep(ri,R) cin >> r[ri];
//     sort(r.rbegin(),r.rend());
//     rep(gi,G) cin >> g[gi];
//     sort(g.rbegin(),g.rend());
//     rep(bi,B) cin >> b[bi];
//     sort(b.rbegin(),b.rend());
//     dfs(0,0,0,0);
//     cout << ans << endl;
// 	return 0;
// }
