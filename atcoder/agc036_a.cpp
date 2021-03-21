// https://atcoder.jp/contests/agc036/tasks/agc036_a
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
	ll S;
	cin >> S;
    ll x1 = 1e9;
    ll y1 = 1;
    ll y2 = (S +(x1-1)) / x1;
    ll x2 = x1 * y2 - S;

    vector<ll> ans;
    ans.push_back(x1); ans.push_back(y1);
    ans.push_back(x2); ans.push_back(y2);
    ans.push_back(0); ans.push_back(0); 

    rep(i, ans.size()) {
    	cout << ans[i] << endl;
    }
	return 0;
}
