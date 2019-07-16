// https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_g
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

long long gcd(long long a, long long b)
{
	if (a < b) {
		a ^= b;
		b ^= a;
		a ^= b;
	}

	return b ? gcd(b, a % b) : a;
}


int main() {
	long long N, A, B, ans;
	cin >> N;

	for (long long i = 0; i < N; i++)
	{
		cin >> A >> B;
		ans = gcd(A, B);
		cout << ans << endl;
	}
}
