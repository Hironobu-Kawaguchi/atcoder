// https://atcoder.jp/contests/abc151/tasks/abc151_d
// #include<iostream>
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;
const int di[] = {-1,0,1,0};
const int dj[] = {0,-1,0,1};
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
	int H, W;
	cin >> H >> W;
    vector<string> S(H);
    rep(i,H) cin >> S[i];
    int ans = 0;
    rep(si,H) rep(sj,W) {
        if (S[si][sj] == '#') continue;
        vector<vector<int>> dist(H, vector<int>(W, INF));
        queue<P> q;
        auto update = [&](int i, int j, int x) {    // lambda関数
            if (dist[i][j] != INF) return;
            dist[i][j] = x;
            q.push(P(i,j)); // .emplace(i,j)
        };
        update(si,sj,0);
        while (!q.empty()) {
            int i = q.front().first;
            int j = q.front().second; q.pop();
            rep(dir,4) {
                int ni = i + di[dir] , nj = j + dj[dir];
                if (ni<0 || ni>=H || nj<0 || nj>=W) continue;
                if (S[ni][nj] == '#') continue;
                update(ni, nj, dist[i][j]+1);
            }
        }
        rep(i,H) rep(j,W) {
            if (dist[i][j] == INF) continue;
            ans = max(ans, dist[i][j]);
        }
    }

	cout << ans << endl;
	return 0;
}
