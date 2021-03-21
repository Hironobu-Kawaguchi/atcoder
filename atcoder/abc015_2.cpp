// https://atcoder.jp/contests/abc015/tasks/abc015_2
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
	vector<int> A(N);
	int sum = 0, cnt = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
		if (A[i] == 0) continue;
		else 
		{
			cnt++;
			sum += A[i];
		}
	}

	int ans = ceil((double)sum / cnt);
	cout << ans << endl;
	return 0;
}
