// https://atcoder.jp/contests/abc106/tasks/abc106_c
#include<iostream>
//#include<algorithm>
//#include <numeric>
#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	string S;
	int K;
	cin >> S >> K;
	char ans;
	for (int i = 0; i < K; i++)
	{
		if (S[i] != '1')
		{
			ans = S[i];
			break;
		}
		else if (i == K - 1)
		{
			ans = S[i];
		}
	}

	cout << ans << endl;
}
