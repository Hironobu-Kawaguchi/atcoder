// https://atcoder.jp/contests/abc112/tasks/abc112_c
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<tuple>
#include<queue>
#include<regex>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int en, H;
	int N;
	cin >> N;

	vector<int> x(N), y(N), h(N);
	for (int i = 0; i < N; i++)
	{
		cin >> x[i] >> y[i] >> h[i];
		if (h[i] > 0) en = i;
	}

	for (int cx = 0; cx <= 100; cx++)
	{
		for (int cy = 0; cy <= 100; cy++)
		{
			H = h[en] + abs(x[en] - cx) + abs(y[en] - cy);
			for (int i = 0; i < N; i++)
			{
				if (max(H - (int)abs(x[i] - cx) - (int)abs(y[i] - cy), 0) != h[i]) break;
				if (i == N-1) {
					cout << cx << ' ' << cy << ' ' << H;
					return 0;
				}
			}
		}
	}
}
