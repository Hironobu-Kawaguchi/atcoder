// https://atcoder.jp/contests/abc139/tasks/abc139_c
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
// #include<math.h>

#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int n;
	cin >> n;
    vector<int> h(n);
    rep(i, n) {
        cin >> h[i];
    }
    int ans = 0, tmp = 0;
    rep(i, n-1) {
        if (h[i] >= h[i+1]) {
            ++tmp;
        } else {
            ans = max(ans, tmp);
            tmp = 0;
        }
    }
    ans = max(ans, tmp);
	cout << ans << endl;
	return 0;
}
