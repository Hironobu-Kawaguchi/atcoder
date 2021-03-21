// https://atcoder.jp/contests/abc085/tasks/abc085_d
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
	int n, h;
	cin >> n >> h;
    vector<int> a(n), b(n);
    rep(i, n) cin >> a[i] >> b[i];

    int a_max = *max_element(all(a));
    sort(all(b));
    reverse(all(b));

    int ans = 0;
    rep(i, n) {
        if (b[i] > a_max) {
            h -= b[i];
            ++ans;
            if (h<=0) break;
        } else break;
    }

    if (h>0) ans += (h + (a_max-1)) / a_max;
	cout << ans << endl;
	return 0;
}
