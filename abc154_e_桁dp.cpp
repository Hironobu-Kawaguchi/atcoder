// https://atcoder.jp/contests/abc154/tasks/abc154_e
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
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int dp[105][4][2];

int main() {
    string s;
    cin >> s;
    int n = s.size();
	int K;
	cin >> K;
    dp[0][0][0] = 1;
    rep(i,n) rep(j,4) rep(k,2) {    // i:桁, j:非0の数, k:0->nと同じ数,1->nより小さい数
        int nd = s[i] - '0';    // nd:nのi桁
        rep(d,10) {
            int ni = i+1, nj = j, nk = k;
            if(d != 0) nj++;    // 非0の数が増える
            if(nj > K) continue;    // 非0の数がKを超えたら計算不要
            if(k == 0) {    // ここまでnと同じ場合
                if(d > nd) continue;    // nより大きくなるのでダメ
                if(d < nd) nk = 1;      // nより小さくなるのでkは1に
            }
            dp[ni][nj][nk] += dp[i][j][k];
        }
    }
    int ans = dp[n][K][0] + dp[n][K][1];
	cout << ans << endl;
	return 0;
}
