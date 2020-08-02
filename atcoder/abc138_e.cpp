// https://atcoder.jp/contests/abc138/tasks/abc138_e
// https://atcoder.jp/contests/abc138/submissions/7013118
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
#include<vector>
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
	string s, t;
	cin >> s >> t;
    int n = s.size(), m = t.size();
    vector<vector<int>> is(26);
    rep(i, n) is[s[i] - 'a'].push_back(i);
    rep(i, n) is[s[i] - 'a'].push_back(i+n);

    ll ans = 0;
    int p = 0;
    rep(i, m) {
        int c = t[i] - 'a';
        if (is[c].size() == 0) {
        	cout << "-1" << endl;
            return 0;
        }
        p = *lower_bound(is[c].begin(), is[c].end(), p) + 1;
        if (p >= n) {
            p -= n;
            ans += n;
        }
    }
    ans += p;
	cout << ans << endl;
	return 0;
}
