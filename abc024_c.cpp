// https://atcoder.jp/contests/abc024/tasks/abc024_c
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD=1e9+7;

int main() {
	int n, d, k;
	cin >> n >> d >> k;
    vector<P> v(d);
    rep(j, d) cin >> v[j].first >> v[j].second;
    rep(i, k) {
        int s, t;
        cin >> s >> t;
        int ans = 0;
        rep(j, d) {
            ans = j;
            if (v[j].first <= s && v[j].second >=s) {
                if (v[j].first <= t && v[j].second >=t) {
                    break;
                } else if (v[j].first > t) {
                    s = v[j].first;
                } else if (v[j].second < t) {
                    s = v[j].second;
                }
            }
        }
    	cout << ans+1 << endl;
    }
	return 0;
}
