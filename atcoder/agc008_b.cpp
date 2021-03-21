// https://atcoder.jp/contests/agc008/tasks/agc008_b
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

int main() {
	int N, K;
	cin >> N >> K;
    vector<ll> a(N);
    rep(i, N) cin >> a[i];

    vector<ll> v(N+1, 0);   // 累積和
    rep(i, N) v[i+1] = v[i] + a[i];
    vector<ll> w(N+1, 0);   // 正の値のみの累積和
    rep(i, N) w[i+1] = w[i] + max(a[i], 0ll);

    ll ans = -LINF;
    rep(i, N-K+1) {
        ll tmp = w[N];
        // Kマスを白or黒に塗る
        tmp += max(v[i+K]-v[i], 0ll);
        tmp -= w[i+K]-w[i];
        ans = max(ans, tmp);
    }
    
	cout << ans << endl;
	return 0;
}
