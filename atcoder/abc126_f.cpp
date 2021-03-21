// https://atcoder.jp/contests/abc126/tasks/abc126_f
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
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int M;
    ll K;
	cin >> M >> K;

    ll x = 1;
    rep(i, M) x *= 2;   // 2**M
    if (!K) {   // K==0 -> 0 0 1 1 ... x-1 x-1
        rep(i, x) cout << i << ' ' << i << ' ';
        cout << endl;
        return 0;
    }
    if (K >= x) {   // K > x-1 -> -1
        cout << -1 << endl;
        return 0;
    }
    ll y = 0;
    rep(i, x) if(i != K) y ^= i;    // y(K以外の0...x-1をXOR)がKでなければ-1
    if (y != K) {
        cout << -1 << endl;
        return 0;
    }

    rep(i, x) if(i!=K) cout << i << ' ';    // K 以外の 0 ... x-1
    cout << K << ' ';
    for (int i = x-1; i >= 0; i--) if(i!=K) cout << i << ' ';   // K 以外の x-1 ... 0
    cout << K << ' ' << endl;
	return 0;
}
