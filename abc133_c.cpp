// https://atcoder.jp/contests/abc133/tasks/abc133_c
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
	int L, R;
	cin >> L >> R;

    ll ans = LINF;
    for (ll i = L; i <= min(R, L+2019); i++) {
        for (ll j = i+1; j <= min(R, L+2019); j++) {
            ans = min(ans, ((i%2019)*(j%2019)%2019));
        }        
    }

	cout << ans << endl;
	return 0;
}
