// A - Buttons
// https://atcoder.jp/contests/abc124/tasks/abc124_a

#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <queue>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int A, B;
	cin >> A >> B;
	if (A == B) {
		cout << A * 2 << endl;
	}
	else {
		cout << max(A, B) * 2 -1 << endl;
	}
	return 0;
}
