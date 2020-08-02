// https://atcoder.jp/contests/abc023/tasks/abc023_c
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
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int R, C, K, N;
	cin >> R >> C >> K;
    cin >> N;
    vector<int> r(N), c(N);
    vector<int> rr(100000), cc(100000);
    rep(i,N) {
        cin >> r[i] >> c[i];
        r[i]--;
        c[i]--;
        rr[r[i]]++;
        cc[c[i]]++;
    }
    vector<ll> rrr(100001), ccc(100001);
    rep(i,R) rrr[rr[i]]++;
    rep(i,C) ccc[cc[i]]++;

    ll ans = 0;
    rep(i, K+1) ans += rrr[i] * ccc[K-i];
    rep(i,N) {
        if (rr[r[i]] + cc[c[i]] == K)   ans--;
        if (rr[r[i]] + cc[c[i]] == K+1) ans++;
    }
	cout << ans << endl;
	return 0;
}
