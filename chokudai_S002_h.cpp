// https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_h
#include<iostream>
#include<algorithm>
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
	long long N, A, B, ans;
	cin >> N;

	for (long long i = 0; i < N; i++)
	{
		cin >> A >> B;

		if (A == B)
		{
			ans = -1;
		}
		else
		{
			ans = abs(A - B);
			//int mx = max(A, B);
			//for (long long j = mx; j > 0; j--)
			//{
			//	if (A % j == B % j)
			//	{
			//		ans = j;
			//		break;
			//	}
			//}
		}

		cout << ans << endl;
	}
}
