// https://atcoder.jp/contests/abc105/tasks/abc105_d
#include<iostream>
//#include<algorithm>
//#include <numeric>
//#include<string>
#include<vector>
#include<map>
//#include<tuple>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	vector<int> A(N);
	for (int i = 0; i < A.size(); i++)
	{
		cin >> A[i];
	}

	map<int, int> m;
	vector<int> SUM(N + 1);
	SUM[0] = 0;
	for (int i = 0; i < N; i++)
	{
		SUM[i + 1] = (SUM[i] + A[i]) % M;
	}

	long long ans = 0;
	for (int i = 0; i < SUM.size(); i++)
	{
		ans += m[SUM[i]];
		m[SUM[i]]++;
	}

	cout << ans << endl;
}
