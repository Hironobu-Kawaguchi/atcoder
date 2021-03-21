// https://atcoder.jp/contests/abc079/tasks/abc079_b
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
	int N;
	cin >> N;

	vector<long long> vec(N+1);

	vec[0] = 2;
	vec[1] = 1;

	for (int i = 2; i < N + 1; i++)
	{
		vec[i] = vec[i - 1] + vec[i - 2];
	}

	cout << vec[N] << endl;
	return 0;
}
