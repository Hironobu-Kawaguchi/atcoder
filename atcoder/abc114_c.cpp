// https://atcoder.jp/contests/abc114/tasks/abc114_c
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<vector>
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

ll N, ans = 0;

void dfs(ll x, ll a, ll b, ll c) {
	if (x > N) return;
	if (a && b && c) ans++;
	dfs(10 * x + 3, 1, b, c);
	dfs(10 * x + 5, a, 1, c);
	dfs(10 * x + 7, a, b, 1);
}

int main() {
	cin >> N;
	dfs(0, 0, 0, 0);
	cout << ans << endl;
	return 0;
}
