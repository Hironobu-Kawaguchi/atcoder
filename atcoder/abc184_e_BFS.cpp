// https://atcoder.jp/contests/abc184/tasks/abc184_e
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

const int di[] = {-1, 0, 1, 0};
const int dj[] = { 0,-1, 0, 1};

int main() {
	int h, w;
    cin >> h >> w;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    vector<vector<int>> dist(h, vector<int>(w, INF));
    queue<P> q;
    rep(i,h) rep(j,w) {
        if (s[i][j] == 'S') {
            q.emplace(i,j);
            dist[i][j] = 0;
        }
    }
    vector<vector<P>> warps(26);
    rep(i,h) rep(j,w) if (islower(s[i][j])) warps[s[i][j] - 'a'].emplace_back(i,j);

    while (!q.empty()) {
        int i = q.front().first;
        int j = q.front().second;
        q.pop();
        if (s[i][j] == 'G') {
            cout << dist[i][j] << endl;
            return 0;
        }
        rep(v,4) {
            int ni = i + di[v], nj = j + dj[v];
            if (ni<0 || ni>=h || nj<0 || nj>=w) continue;
            if (s[ni][nj] == '#') continue;
            if (dist[ni][nj] != INF) continue;
            dist[ni][nj] = dist[i][j] + 1;
            q.emplace(ni,nj);
        }

        if (islower(s[i][j])) {
            for (P p : warps[s[i][j] - 'a']) {
                int ni = p.first, nj = p.second;
                if (ni<0 || ni>=h || nj<0 || nj>=w) continue;
                if (s[ni][nj] == '#') continue;
                if (dist[ni][nj] != INF) continue;
                dist[ni][nj] = dist[i][j] + 1;
                q.emplace(ni,nj);
            }
            warps[s[i][j] - 'a'] = vector<P>();
        }
    }
    cout << -1 << endl;
	return 0;
}
