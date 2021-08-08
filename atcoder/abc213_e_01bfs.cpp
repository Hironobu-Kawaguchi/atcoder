// https://atcoder.jp/contests/abc213/tasks/abc213_e
// https://atcoder.jp/contests/abc213/submissions/24849890
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

const int di[] = {-1,0,1,0};
const int dj[] = {0,-1,0,1};

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	int h, w;
	cin >> h >> w;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    deque<P> q;
    vector dist(h, vector<int>(w, INF));
    vector visited(h, vector<bool>(w));

    dist[0][0] = 0;
    q.emplace_back(0,0);
    while (q.size()) {
        auto [i,j] = q.front(); q.pop_front();
        if (visited[i][j]) continue;
        visited[i][j] = true;
        int d = dist[i][j];
        rep(v,4) {
            int ni = i+di[v], nj = j+dj[v];
            if (ni<0 || nj<0 || ni>=h || nj>=w) continue;
            if (s[ni][nj]=='#') continue;
            if (dist[ni][nj]<=d) continue;
            dist[ni][nj] = d;
            q.emplace_front(ni,nj);
        }
        for (int ei = -2; ei <= 2; ++ei) {
            for (int ej = -2; ej <= 2; ++ej) {
                if (abs(ei)+abs(ej)>3) continue;
                int ni = i+ei, nj = j+ej;
                if (ni<0 || nj<0 || ni>=h || nj>=w) continue;
                if (dist[ni][nj]<=d+1) continue;
                dist[ni][nj] = d+1;
                q.emplace_back(ni,nj);
            }
        }
    }
    cout << dist[h-1][w-1] << endl;
	return 0;
}
