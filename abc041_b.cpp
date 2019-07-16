// https://atcoder.jp/contests/abc041/tasks/abc041_b
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<queue>
// #include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	long long A, B, C;
	cin >> A >> B >> C;

	long long ans;
	long long mod = pow(10, 9) + 7;
	ans = A * B % mod;
	ans = ans * C % mod;

	cout << ans << endl;
	return 0;
}
