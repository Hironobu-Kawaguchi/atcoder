// https://atcoder.jp/contests/abc061/tasks/abc061_d
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
	int N, M;
	cin >> N >> M;

    vector<int> a(M), b(M);
    vector<ll> c(M);

    rep(i, M) {
        cin >> a[i] >> b[i] >> c[i];
        a[i] = a[i] - 1;
        b[i] = b[i] - 1;
        c[i] = -c[i];
    }

    vector<ll> dist(N);
    rep(i, N) dist[i] = LINF;
    dist[0] = 0;

    rep(loop, N-1) {
        rep(i, M) {
            if (dist[a[i]] == LINF) continue;
            if (dist[b[i]] > dist[a[i]] + c[i]) dist[b[i]] = dist[a[i]] + c[i];
        }
    } 
    ll ans = dist[N-1];

    vector<bool> negative(N);
    rep(i, N) negative[i] = false;
    rep(loop, N) {
        rep(i, M) {
            if (dist[a[i]] == LINF) continue;
            if (dist[b[i]] > dist[a[i]] + c[i]) {
                dist[b[i]] = dist[a[i]] + c[i];
                negative[b[i]] = true;
            }
            if (negative[a[i]] == true) negative[b[i]] = true;
        }
    }

    if (negative[N-1])
    	cout << "inf" << endl;
    else
    	cout << -ans << endl;
	return 0;
}
