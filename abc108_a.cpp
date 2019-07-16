// https://atcoder.jp/contests/abc108/tasks/abc108_a
#include<iostream>
//#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	int K;
	cin >> K;

	int ans = K / 2;
	ans = (K - ans) * ans;

	cout << ans << endl;
}
