// https://atcoder.jp/contests/abc143/tasks/abc143_d
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
	int N;
	cin >> N;
    vector<int> L(N);
    rep (i, N) {
        cin >> L[i];
    }
    sort(all(L));

    ll ans = 0;
    rep (i, N-1) {
        for (int j = i+1; j < N; j++) {
            int p = L[i] + L[j];
            int idx = lower_bound(L.begin(), L.end(), p) - L.begin();
            idx -= j + 1;
            ans += idx;
        }
    }

	cout << ans << endl;
	return 0;
}
