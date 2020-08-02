// https://atcoder.jp/contests/abc036/tasks/abc036_a
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
	int A, B;
	cin >> A >> B;

	int ans = ceil((double)B / A);
	cout << ans << endl;

	return 0;
}
