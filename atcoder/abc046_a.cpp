// https://atcoder.jp/contests/abc046/tasks/abc046_a
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
#include<set>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;


int main() {
	// 入力
	int a, b, c;
	cin >> a >> b >> c;

	set<int> abc;
	abc.insert(a);
	abc.insert(b);
	abc.insert(c);

	int ans = abc.size();
	cout << ans << endl;

	return 0;
}
