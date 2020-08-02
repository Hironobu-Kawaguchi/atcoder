// https://atcoder.jp/contests/apg4b/tasks/APG4b_ca
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
	int N;
	cin >> N;
	vector < pair<ll, ll>> p(N);
	rep(i, N) {
		ll a, b;
		cin >> a >> b;
		p[i] = make_pair(b, a);
	}
	sort(p.begin(), p.end());
	rep(i, N) {
		cout << p[i].second << " " << p[i].first << endl;
	}
	return 0;
}
