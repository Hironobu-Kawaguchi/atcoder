// https://atcoder.jp/contests/abc063/tasks/arc075_b
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

ll N, A, B;
vector<ll> h;

bool f(ll K) {
    ll tmp = 0;
    rep(i, N) {
        ll rem = h[i] - B*K;
        if (rem > 0) tmp += (rem + (A-B-1)) / (A-B);
    }
    return (tmp <= K);
}

ll binary_search(ll ok, ll ng) {
    while (abs(ok - ng) > 1) {
        ll mid = (ok + ng) / 2;
        if (f(mid)) ok = mid;
        else ng = mid;
    }
    return ok;
}

int main() {
	cin >> N >> A >> B;
    h = vector<ll>(N);   // サイズNを確保
    rep(i, N) cin >> h[i];
	cout << binary_search(INF, 0) << endl;
	return 0;
}
