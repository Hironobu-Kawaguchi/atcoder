// https://atcoder.jp/contests/abc041/tasks/abc041_c
#include<iostream>
#include<algorithm>
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
	vector<pair<int, int>> a(N);
	for (int i = 0; i < N; i++)
	{
		int tmp;
		cin >> tmp;
		a[i] = make_pair(tmp, i +1);
	}

	sort(a.begin(), a.end());
	reverse(a.begin(), a.end());

	for (int i = 0; i < N; i++)
	{
		cout << a[i].second << endl;
	}

	return 0;
}
