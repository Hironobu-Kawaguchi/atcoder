// https://atcoder.jp/contests/abc105/tasks/abc105_c
#include<iostream>
//#include<algorithm>
//#include <numeric>
#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>
//#include<cstdio>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N;
	cin >> N;
	string ans = "";
	while (N != 0) {
		if (N % 2 != 0) {
			N--;
			ans = "1" + ans;
		}
		else ans = "0" + ans;
		N /= -2;
	}

	if (ans == "") ans = "0";

	cout << ans << endl;
	return 0;
}
