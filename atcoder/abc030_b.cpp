// https://atcoder.jp/contests/abc030/tasks/abc030_b
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
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
	int n, m;
	cin >> n >> m;

	n = n % 12;
	double nd, md, ans;
	nd = (double)n * 360 / 12 + (double)m * 360 / 12 / 60;
	md = (double)m * 360 / 60;
	ans = min(abs(nd - md), 360 - abs(nd - md));

	cout << ans << endl;

	return 0;
}
