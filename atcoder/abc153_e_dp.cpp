// https://atcoder.jp/contests/abc153/tasks/abc153_e
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

const int MAXH = 10000;
const int MAXN = 1000;
vector<vector<int>> dp(MAXN+1, vector<int>(MAXH+1, INF));

int main() {
	int H, N;
	cin >> H >> N;
	vector<int> A(N), B(N);
	int mxa=0, mxb=1000;
	rep(i,N) {
		cin >> A[i] >> B[i];
		if (A[i]*mxb > mxa*B[i]) {
			mxa = A[i];
			mxb = B[i];
		}
	} 
	rep(i,N+1) {
		dp[i][0] = 0;
	}
	rep(i,N) {
		rep(j,H+1) {
			if (j >= A[i]) {
				dp[i+1][j] = min(dp[i][j], dp[i+1][j-A[i]] + B[i]);
			} else {
				dp[i+1][j] = min(dp[i][j], (j+A[i]-1)/A[i]*B[i]);
			}
		}
	}
	cout << dp[N][H] << endl;
	return 0;
}
