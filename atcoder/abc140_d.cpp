// https://atcoder.jp/contests/abc140/tasks/abc140_d
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
	int N, K;
	cin >> N >> K;
	string S;
	cin >> S;

	int ans = N-1;
	rep(i, N-1) {
		if (S[i] != S[i + 1]) ans -= 1;
	}

	ans = min(N-1, ans + 2 * K);
	cout << ans << endl;
	return 0;
}
