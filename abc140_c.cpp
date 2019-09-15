// https://atcoder.jp/contests/abc140/tasks/abc140_c
#include<iostream>
#include<algorithm>
//#include <numeric>
#include<vector>
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

	vector<int> B(N-1);
	rep(i, N-1) {
		cin >> B[i];
	}

	int ans = B[0] + B[N-2];
	rep(i, N-2) {
		ans += min(B[i], B[i+1]);
	}

	cout << ans << endl;
	return 0;
}
