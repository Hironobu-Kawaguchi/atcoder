// https://atcoder.jp/contests/abc143/tasks/abc143_e
// https://atcoder.jp/contests/abc143/submissions/8034843
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
#define all(v) (v).begin(),(v).end()
#define chmin(x,y) x = min(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
    int N, M, L;
	cin >> N >> M >> L;
    vector<vector<int>> fuel(N, vector<int>(N, INF));
    rep (i, N) fuel[i][i] = 0;

    rep (i, M) {
        int A, B, C;
        cin >> A >> B >> C;
        A--; B--;
        fuel[A][B] = fuel[B][A] = C;
    }

    // ワーシャルフロイド法
    rep (i, N) rep (j, N) rep (k, N) {
        chmin(fuel[j][k], fuel[j][i] + fuel[i][k]);
    }

    vector<vector<int>> dist(N, vector<int>(N, INF));
    rep (i, N) rep(j, N) {
        if (i==j) dist[i][j] = 0;
        else if (fuel[i][j] <= L) dist[i][j] = 1;
    }

    // ワーシャルフロイド法
    rep (i, N) rep(j, N) rep(k, N) {
        chmin(dist[j][k], dist[j][i] + dist[i][k]);
    }

    int Q;
    cin >> Q;
    rep (i, Q) {
        int s, t;
        cin >> s >> t;
        s--; t--;
        if(dist[t][s] < INF) cout << dist[t][s] - 1 << endl;
        else cout << -1 << endl;
    }
	return 0;
}
