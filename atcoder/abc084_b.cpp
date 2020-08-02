// https://atcoder.jp/contests/abc084/tasks/abc084_b
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<tuple>
#include<queue>
#include <regex>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	string A, B, S;
	cin >> A >> B >> S;
	if (regex_match(S, regex("\\d{" + A + "}-\\d{" + B + "}"))) {
		cout << "Yes" << endl;
	}
	else cout << "No" << endl;
}
