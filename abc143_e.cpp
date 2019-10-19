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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

template<class T>
inline bool chmax(T &a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
inline bool chmin(T &a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}

ll N, M, L, Q;
ll fuel[305][305];
ll dist[305][305];
ll s[105000], t[105000];
ll A[100000], B[100000], C[100000];

int main() {
	cin >> N >> M >> L;
    rep (i, M) {
        cin >> A[i] >> B[i] >> C[i];
        A[i] -= 1;
        B[i] -= 1;
    }
    cin >> Q;
    rep (i, Q) {
        cin >> s[i] >> t[i];
        s[i] -= 1;
        t[i] -= 1;
    }

    rep (i, N) {
        rep (j, N) {
            fuel[i][j] = LINF;
            dist[i][j] = LINF;
        }
        fuel[i][i] = 0;
        dist[i][i] = 0;
    }
    rep (i, M) {
        chmin(fuel[A[i]][B[i]], C[i]);
        chmin(fuel[B[i]][A[i]], C[i]);
    }
    rep (i, N) rep (j, N) rep (k, N) {
        chmin(fuel[j][k], fuel[j][i] + fuel[i][k]);
    }
    rep (i, N) rep(j, N) {
        if (i==j) continue;
        if (fuel[i][j] <= L) chmin(dist[i][j], 1LL);
    }
    rep (i, N) rep(j, N) rep(k, N) {
        chmin(dist[j][k], dist[j][i] + dist[i][k]);
    }

    rep(i, Q) {
        if(dist[t[i]][s[i]] < LINF) cout << dist[t[i]][s[i]] - 1 << endl;
        else cout << -1 << endl;
    }
	return 0;
}
