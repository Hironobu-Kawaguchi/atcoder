// A - Between Two Integers
// https://atcoder.jp/contests/abc061/tasks/abc061_a

#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <queue>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int A, B, C;
	cin >> A >> B >> C;
	if (A <= C && B >= C) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
	return 0;
}
