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

const int MAX = 1000;

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int h, w;
    cin >> h >> w;
	int sy, sx, gy, gx;
	cin >> sy >> sx >> gy >> gx;
	sy--, sx--, gy--, gx--;
	vector<string> S(h);
    rep(i,h) cin >> S[i];
	queue<tuple<int, int>> Q;
    bool visited[h][w];
    rep(y,h) rep(x,w) visited[y][x] = false;
    int c[h][w];  // クラスター番号
    rep(y,h) rep(x,w) c[y][x] = -1;

    int ccnt = 0;
    rep(cy,h) rep(cx,w) {
        if (S[cy][cx]=='#') continue;
        if (visited[cy][cx]) continue;
        ccnt++;
    	Q.emplace(cy, cx);
        while (!Q.empty()) {
            int y, x;
            tie(y, x) = Q.front();
            Q.pop();
            if (visited[y][x]) continue;
            visited[y][x] = true;
            c[y][x] = ccnt - 1;   // クラスター番号は0開始に
            vector<int> vy{ 0, 0, -1, +1 };
            vector<int> vx{ -1, +1, 0, 0 };
            for (int i = 0; i < 4; i++) {
                int newx = x + vx[i];
                int newy = y + vy[i];
                if (0 <= newx && newx < w && 0 <= newy && newy < h && S[newy][newx] != '#') {
                    Q.emplace(newy, newx);
                }
            }
        }
    }

    rep(y,h) {
        rep(x,w) cout << c[y][x] << ' ';
        cout << endl;
    } 

    int sc = c[sy][sx], gc = c[gy][gx];
    bool to[ccnt][ccnt];
    rep(i,ccnt) rep(j,ccnt) to[i][j] = false;
    rep(y,h-2) rep(x,w) {
        if (S[y][x]=='#') continue;
        rep(vy,3) rep(vx,5) {
            int newx = x + vx - 2;
            int newy = y + vy;
            if (newx<0 || newx>=w) continue;
            if (S[newy][newx]=='#') continue;
            to[c[y][x]][c[newy][newx]] = true;
            to[c[newy][newx]][c[y][x]] = true;
        }
    }

    rep(i,ccnt) {
        rep(j,ccnt) cout << to[i][j] << ' ';
        cout << endl;
    } 
    cout << sc << " -> " << gc << endl;

    int ans = 0;
	queue<int> QC;
    bool visitedc[ccnt];
    rep(i,ccnt) visitedc[i] = false;

    QC.emplace(sc);
    while (!QC.empty()) {
        int now;
        now = QC.front();
        QC.pop();
        if (now==gc) {    // Goal!!!
            cout << ans << "\n";
            return 0;
        }
        if (visitedc[now]) continue;
        visitedc[now] = true;
        ans++;
        rep(i,ccnt) {
            if (to[now][i]==true && visitedc[i]==false) {
                QC.emplace(i);
            }
        }
    }

    cout << -1 << "\n";
	return 0;
}
