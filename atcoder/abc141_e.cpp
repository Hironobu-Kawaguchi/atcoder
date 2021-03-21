// https://atcoder.jp/contests/abc141/tasks/abc141_e
#include<iostream>
#include<algorithm>
//#include<string>
//#include <numeric>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>
//#include <bitset>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
	int N;
	cin >> N;
	string S;
	cin >> S;

	int ans = 0;
	rep(i, N - 1) {
		for (int j = i + 1 + ans; j < N - ans; j++) {
			for (int l = ans + 1; l <= min(j - i, N - j); l++) {
				bool chk = true;
				rep(k, l) {
					if (S[i + k] != S[j + k]) {
						chk = false;
						break;
					}
				}
				if (chk) {
					ans = max(ans, l);
				}
				else {
					break;
				}
			}
		}
	}

	cout << ans << endl;
	return 0;
}
