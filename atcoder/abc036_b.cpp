// https://atcoder.jp/contests/abc036/tasks/abc036_b
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;


int main() {
	// 入力
	int N;
	cin >> N;

	vector<string> s(N), ans(N);
	rep(i, N) {
		cin >> s[i];
	}

	rep(i, N) {
		rep(j, N) {
			ans[j] += s[N-i-1][j];
		}
	}

	rep(j, N) {
		cout << ans[j] << endl;
	}

	return 0;
}
