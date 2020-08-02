// https://atcoder.jp/contests/abc038/tasks/abc038_c
#include<iostream>
//#include<algorithm>
//#include<string>
#include<vector>
//#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	long long N;
	cin >> N;
	vector<long long> a(N), sum(N), tmp(N);
	for (long long i = 0; i < N; i++)
	{
		cin >> a[i];
		if (i == 0)
		{
			sum[i] = 1;
			tmp[i] = 1;
		}
		else if (a[i] > a[i-1])
		{
			tmp[i] = tmp[i - 1] + 1;
			sum[i] = sum[i - 1] + tmp[i];
		}
		else {
			tmp[i] = 1;
			sum[i] = sum[i - 1] + tmp[i];
		}
	}

	cout << sum[N-1] << endl;
	return 0;
}
