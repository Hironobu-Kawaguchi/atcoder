// https://atcoder.jp/contests/abc046/tasks/abc046_b
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
	int N, K;
	cin >> N >> K;

	ll ans = K * pow((K - 1), (N - 1));

	cout << ans << endl;

	return 0;
}
