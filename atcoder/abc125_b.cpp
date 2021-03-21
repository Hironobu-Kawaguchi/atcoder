// https://atcoder.jp/contests/abc125/tasks/abc125_b
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
	int N;
	cin >> N;
	vector<int> V(N), C(N);
	int ans = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> V[i];
	}
	for (int i = 0; i < N; i++)
	{
		cin >> C[i];
		if (V[i] > C[i])
		{
			ans += V[i] - C[i];
		}
	}
	cout << ans << endl;
	return 0;
}
