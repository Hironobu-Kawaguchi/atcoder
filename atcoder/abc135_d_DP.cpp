// https://atcoder.jp/contests/abc135/tasks/abc135_d
// https://atcoder.jp/contests/abc135/submissions/6584488
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

const int N = 13;
const int mod = 1000000007;


int main() {
	// 入力
	string S;
	cin >> S;

	int dp[N];	// DPテーブル
	memset(dp, 0, sizeof(dp));
	dp[0] = 1;

	// 動的計画法(DP)
	int mul = 1;
	rep(i, (int)S.size()) {
		int nextDP[N];
		memset(nextDP, 0, sizeof(nextDP));
		if (S[S.size() - i -1] == '?') {
			rep(k, 10) {
				rep(j, N) {
					nextDP[(k * mul + j) % N] += dp[j];
					nextDP[(k * mul + j) % N] %= mod;
				}
			}
		}
		else {
			int k = S[(int)S.size() - i - 1] - '0';
			rep(j, N) {
				nextDP[(k * mul + j) % N] += dp[j];
				nextDP[(k * mul + j) % N] %= mod;
			}
		}
		mul *= 10;
		mul %= N;
		rep(j, N) {
			dp[j] = nextDP[j];
		}
	}
	cout << dp[5] << endl;

	return 0;
}
