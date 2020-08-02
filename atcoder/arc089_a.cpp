// https://atcoder.jp/contests/abc086/tasks/arc089_a
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
	int N;
	cin >> N;
	int t, x, y;
	int _t = 0, _x = 0, _y = 0;
	bool flg = true;

	for (int i = 0; i < N; i++)
	{
		cin >> t >> x >> y;
		int xy = abs(x - _x) + abs(y - _y);
		int tt = t - _t;
		if (tt >= xy && (tt - xy) % 2 == 0) continue;
		else {
			flg = false;
			break;
		}
		_t = t;
		_x = x;
		_y = y;
	}

	if (flg) cout << "Yes" << endl;
	else     cout << "No" << endl;
	return 0;
}
