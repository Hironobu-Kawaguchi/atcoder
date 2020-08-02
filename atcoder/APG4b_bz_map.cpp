// https://atcoder.jp/contests/apg4b/tasks/APG4b_bz
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
	int N;
	cin >> N;
	map<int, int> cnt;
	rep(i, N) {
		int a;
		cin >> a;
		if (cnt.count(a)) {
			cnt[a]++;
		}
		else {
			cnt[a] = 1;
		}
	}
	int max_cnt = 0;
	int ans = -1;
	for (auto p : cnt) {
		if (p.second > max_cnt) {
			max_cnt = p.second;
			ans = p.first;
		}
	}
	cout << ans << " " << max_cnt << endl;
	return 0;
}
