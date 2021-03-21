// https://atcoder.jp/contests/abc105/tasks/abc105_b
#include<iostream>
//#include<algorithm>
//#include <numeric>
//#include<string>
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
	string ans = "No";
	for (int i = 0; i < N / 4 + 1; i++)
	{
		if ((N- i * 4) % 7 == 0)
		{
			ans = "Yes";
			break;
		}
	}

	cout << ans << endl;

}
