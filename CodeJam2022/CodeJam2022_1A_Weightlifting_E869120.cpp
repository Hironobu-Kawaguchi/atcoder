#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

long long N, W;
long long A[109][109];
long long dp[109][109];
long long MinA[109][109][109];

void Solve(int TestNum) {
	// Step #1. Input
	cin >> N >> W;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= W; j++) cin >> A[i][j];
	}

	// Step #2. Initialize
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			for (int k = 1; k <= W; k++) MinA[i][j][k] = (1 << 29);
		}
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) dp[i][j] = (1 << 29);
		dp[i][i] = 0;
	}

	// Step #3. Maeshori
	for (int k = 1; k <= W; k++) {
		for (int i = 1; i <= N; i++) {
			MinA[i][i][k] = A[i][k];
			for (int j = i + 1; j <= N; j++) {
				MinA[i][j][k] = min(MinA[i][j - 1][k], A[j][k]);
			}
		}
	}
	
	// Step #3. Dynamic Programming
	for (int haba = 1; haba <= N - 1; haba++) {
		for (int l = 1; l <= N - haba; l++) {
			int r = l + haba;
			for (int m = l; m <= r - 1; m++) {
				long long c1 = dp[l][m + 0];
				long long c2 = dp[m + 1][r];
				long long c3 = 0;
				for (int k = 1; k <= W; k++) c3 += MinA[l][m + 0][k] - MinA[l][r][k];
				for (int k = 1; k <= W; k++) c3 += MinA[m + 1][r][k] - MinA[l][r][k];
				dp[l][r] = min(dp[l][r], c1 + c2 + c3);
			}
		}
	}

	// Output
	long long Answer = dp[1][N];
	for (int i = 1; i <= W; i++) Answer += MinA[1][N][i];
	cout << "Case #" << TestNum << ": " << 2LL * Answer << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		Solve(i);
	}
	return 0;
}