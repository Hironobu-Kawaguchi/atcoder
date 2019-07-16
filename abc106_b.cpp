// https://atcoder.jp/contests/abc106/tasks/abc106_b
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
	int N;
	cin >> N;
	int ans = 0;
	int cnt;
	for (int i = 1; i < N+1; i += 2)
	{
		cnt = 0;
		for (int j = 1; j < i+1; j++)
		{
			if (i % j == 0)
			{
				cnt++;
			}
		}
		if (cnt == 8)
		{
			ans++;
		}
	}

	cout << ans << endl;
}
