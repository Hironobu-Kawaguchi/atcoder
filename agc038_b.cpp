// https://atcoder.jp/contests/agc038/tasks/agc038_b
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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
const ll MOD = 1e9+7;

int main() {
	int n, k;
	cin >> n >> k;
    vector<int> v(n+1);
    rep(i, n) {
        cin >> v[i];
    }
    v[n] = n;

    set<int> num;
    int ans = 1;

    rep(i, k) num.insert(v[i]);
    rep(i, n-k) {
        if (v[i] != *num.begin() || v[i+k] < *--num.end()) ++ans;
        num.erase(v[i]);
        num.insert(v[i+k]);
    }
    bool flg = 0;
    int pre = -1, cnt = 0;
    rep(i, n) {
        if (pre < v[i]) ++cnt;
        else cnt = 1;
        pre = v[i];
        if (cnt == k) {
            flg = 1;
            --ans;
        }
    }
    cout << ans + flg << endl;

	return 0;
}
