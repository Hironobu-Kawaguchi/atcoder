// https://atcoder.jp/contests/abc137/tasks/abc137_c
// https://atcoder.jp/contests/abc137/submissions/6835088
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
	int n;
	cin >> n;
	map<string, int> mp;
	rep(i, n) {
		string s;
		cin >> s;
		sort(s.begin(), s.end());
		mp[s]++;
	}
	ll ans = 0;
	for (auto& p : mp) {
		int s = p.second;
		ans += (ll)s * (s - 1) / 2;
	}
	cout << ans << endl;
	return 0;
}
