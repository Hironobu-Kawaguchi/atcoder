// https://atcoder.jp/contests/tdpc/tasks/tdpc_game
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MX = 1005;
int a[MX], b[MX], dp[MX][MX];

int main() {
	int na, nb;
	cin >> na >> nb;
    rep(i,na) cin >> a[i];
    rep(i,nb) cin >> b[i];

    drep(i,na+1) drep(j,nb+1) {
        if (i==na && j==nb) continue;
        if((i+j)&1) {
            dp[i][j] = INF;
            if(i<na) dp[i][j] = min(dp[i+1][j], dp[i][j]);
            if(j<nb) dp[i][j] = min(dp[i][j+1], dp[i][j]);
        } else {
            dp[i][j] = 0;
            if(i<na) dp[i][j] = max(dp[i+1][j] + a[i], dp[i][j]);
            if(j<nb) dp[i][j] = max(dp[i][j+1] + b[j], dp[i][j]);
        }
    }

	cout << dp[0][0] << endl;
	return 0;
}
