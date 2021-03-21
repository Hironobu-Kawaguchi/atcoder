// https://atcoder.jp/contests/agc037/tasks/agc037_a
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
// #include<assert.h>
#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD=1e9+7;

int main() {
	string s;
    cin >> s;
    int ans = 0;
    string t, p = "";
    rep(i, s.size()) {
        t += s[i];
        if (t == p) continue;
        p = t;
        t = "";
        ++ans;
    }
	cout << ans << endl;
	return 0;
}
