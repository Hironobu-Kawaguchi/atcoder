// https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
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
	int R, G, B, N;
	cin >> R >> G >> B >> N;

	int ans = 0;

	for (int r = 0; r < N / R + 1; r++)
	{
		int tmp = N - (R * r);
		if (tmp < 0) break;
		for (int g = 0; g < tmp / G + 1; g++)
		{
			int tmp = N - (R * r + G * g);
			if (tmp < 0) break;
			if (tmp % B == 0) ans++;
		}
	}

	cout << ans << endl;
	return 0;
}
