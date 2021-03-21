// https://atcoder.jp/contests/abc113/tasks/abc113_d
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

int main() {
	int H, W, K;
	cin >> H >> W >> K;
	vector<vector<int> > dp(H + 1, vector<int>(W, 0)); dp[0][0] = 1;
	for (int i = 0; i < H; ++i) {
		for (int j = 0; j < W; ++j) {
			for (int k = 0; k < 1 << (W - 1); ++k) {
				// Check if two horizontal lines are connecting
				// 2 つの横線がつながっていないか調べる
				bool ok = true;
				for (int l = 0; l < W - 2; ++l) {
					if (((k >> l) & 1) && ((k >> (l + 1)) & 1)) {
						ok = false;
					}
				}
				if (ok) {
					if (j >= 1 && ((k >> (j - 1)) & 1)) {
						// The case which goes left
						// 左方向に横線をたどるケース
						dp[i + 1][j - 1] += dp[i][j];
						dp[i + 1][j - 1] %= MOD;
					}
					else if (j <= W - 2 && ((k >> j) & 1)) {
						// The case which goes right
						// 右方向に横線をたどるケース
						dp[i + 1][j + 1] += dp[i][j];
						dp[i + 1][j + 1] %= MOD;
					}
					else {
						// The case which goes straight
						// 横線をたどらないケース
						dp[i + 1][j] += dp[i][j];
						dp[i + 1][j] %= MOD;
					}
				}
			}
		}
	}
	cout << dp[H][K - 1] << '\n';
	return 0;
}
