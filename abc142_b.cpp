// https://atcoder.jp/contests/abc142/tasks/abc142_b
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
	int N, K;
	cin >> N >> K;
    vector<int> h(N);
    rep(i, N) cin >> h[i];

    int ans = 0;
    rep(i, N) {
        if (h[i] >= K) ++ans;
    }
	cout << ans << endl;
	return 0;
}
