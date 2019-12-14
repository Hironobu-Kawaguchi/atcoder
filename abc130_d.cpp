// https://atcoder.jp/contests/abc130/tasks/abc130_d
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
	int N;
    ll K;
	cin >> N >> K;
    vector<ll> a(N);
    rep(i,N) cin >> a[i];

    // 尺取法
    ll ans = 0;
    ll sum = 0;
    int r = 0;
    rep(l,N) {
        while(sum<K) {
            if(r==N) break;
            else {
                sum += a[r];
                r++;
            }
        }
        if(sum<K) break;
        ans += N-r+1;
        sum -= a[l];
    }

	cout << ans << endl;
	return 0;
}
