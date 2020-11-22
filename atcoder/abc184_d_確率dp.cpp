// https://atcoder.jp/contests/abc184/tasks/abc184_d
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
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int X = 100;
double dp[X+1][X+1][X+1];

int main() {
	int a, b, c;
	cin >> a >> b >> c;
    for (int i = X-1; i>=0; --i) {
        for (int j = X-1; j>=0; --j) {
            for (int k = X-1; k>=0; --k) {
                if ((i+j+k) == 0) continue;
                double now = 0;
                now += dp[i+1][j][k]*i;
                now += dp[i][j+1][k]*j;
                now += dp[i][j][k+1]*k;
                dp[i][j][k] = now/(i+j+k) + 1;
            }
        }
    }
    double ans = dp[a][b][c];
    printf("%.10f\n", ans);
	return 0;
}
