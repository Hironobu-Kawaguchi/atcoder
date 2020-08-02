// https://atcoder.jp/contests/arc043/tasks/arc043_a
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
	int N;
    ll A, B;
	cin >> N >> A >> B;
    vector<ll> S(N);
    ll mx = 0, mn = LINF, sm = 0;
    rep(i, N) {
        cin >> S[i];
        mx = max(mx, S[i]);
        mn = min(mn, S[i]);
        sm += S[i];
    }

    if (mx == mn) cout << -1 << endl;
    else {
        double P, Q;
        P = (double) B / (mx-mn);
        Q = (double) A - (P * sm / N);

        cout << fixed << setprecision(10) << P << ' ' << Q << endl;
    }
	return 0;
}
