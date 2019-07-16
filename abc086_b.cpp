// https://atcoder.jp/contests/abc086/tasks/abc086_b
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<tuple>
#include<queue>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	int keta = log10(b);
	int y = a * pow(10, keta + 1) + b;

	int x = sqrt(y);

	if (pow(x, 2) == y) cout << "Yes" << endl;
	else           cout << "No" << endl;
	return 0;
}
