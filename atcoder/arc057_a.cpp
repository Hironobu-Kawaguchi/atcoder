// https://atcoder.jp/contests/arc057/tasks/arc057_a
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
    const ll goal = 2000000000000;
	ll A, K;
	cin >> A >> K;

    ll tmp = A;
    ll ans = 0;
    if (K==0) ans = goal - A;
    else {
        while (tmp < goal) {
            tmp += 1 + tmp * K;
            ans++;
        }
    }

	cout << ans << endl;
	return 0;
}
