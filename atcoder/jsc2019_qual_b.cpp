// https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_b
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
	int N;
    ll K;
	cin >> N >> K;
    vector<int> A(N);
    rep(i, N) cin >> A[i];

    ll cnt = 0;
    rep(i, N-1) {
        for (int j = i+1; j < N; j++) {
            if (A[i] > A[j]) cnt++;
        }
    }
    ll ans = cnt * K % MOD;
    cnt = 0;
    rep(i, N) {
        rep(j, N) {
            if (A[i] > A[j]) cnt++;
        }
    }
    ans += K*(K-1)/2 % MOD * cnt % MOD;
    ans %= MOD;

	cout << ans << endl;
	return 0;
}
