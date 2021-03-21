// https://atcoder.jp/contests/abc140/tasks/abc140_b
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

	vector<int> A(N);
	rep(i, N) {
		cin >> A[i];
	}
	vector<int> B(N);
	rep(i, N) {
		cin >> B[i];
	}
	vector<int> C(N);
	rep(i, N-1) {
		cin >> C[i];
	}

	int ans = 0;
	rep(i, N) {
		ans += B[i];
	}
	rep(i, N - 1) {
		if (A[i] + 1 == A[i + 1]) ans += C[A[i]-1];
	}
	cout << ans << endl;
	return 0;
}
