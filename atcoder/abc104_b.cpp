// https://atcoder.jp/contests/abc104/tasks/abc104_b
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
	string S;
	cin >> S;
	int n = S.size();
	string ans = "AC";

	if (S[0] != 'A')
	{
		ans = "WA";
	}

	int cnt = 0;
	for (int i = 1; i < n; i++)
	{
		if (S[i] == 'C' and (i >= 2 and i <= n - 2))
		{
			cnt++;
		}
		else if (S[i] >= 'a' and S[i] <= 'z')
		{
			continue;
		}
		else
		{
			ans = "WA";
		}
	}
	if (cnt != 1)
	{
		ans = "WA";
	}

	cout << ans << endl;
}
