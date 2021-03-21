// https://atcoder.jp/contests/abc176/tasks/abc176_d
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
    int h, w;
    cin >> h >> w;
	int sy, sx, gy, gx;
	cin >> sy >> sx >> gy >> gx;
	--sy, --sx, --gy, --gx;
	vector<string> S(h);
    rep(i,h) cin >> S[i];
    vector<vector<int>> dist(h, vector<int>(w, INF));
    vector<int> vy{ 0, 0, -1, +1 };
    vector<int> vx{ -1, +1, 0, 0 };
    deque<P> q;
    dist[sy][sx] = 0;
    q.emplace_back(sy, sx);
    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        int d = dist[y][x];
        q.pop_front();
        rep(v,4) {
            int ny = y + vy[v], nx = x + vx[v];
            if (ny<0 || ny>=h || nx<0 || nx>=w) continue;
            if (S[ny][nx]=='#') continue;
            if (dist[ny][nx]<=d) continue;
            dist[ny][nx] = d;
            q.emplace_front(ny,nx);
        }
        rep(i,5) rep(j,5) {
            int ny = y + i - 2, nx = x + j - 2;
            if (ny<0 || ny>=h || nx<0 || nx>=w) continue;
            if (S[ny][nx]=='#') continue;
            if (dist[ny][nx]<=d+1) continue;
            dist[ny][nx] = d+1;
            q.emplace_back(ny,nx);
        }
    }
    int ans = dist[gy][gx];
    if (ans==INF) ans = -1;
	cout << ans << "\n";
	return 0;
}
