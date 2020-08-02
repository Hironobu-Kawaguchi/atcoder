// https://atcoder.jp/contests/abc125/tasks/abc126_c
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
	long long N, K;
	cin >> N >> K;
	double ans = 0;

	if (N > K) ans += (double)(N - K);
	for (long long i = 1; i <= min(N, K); i++)
	{
		int logk = ceil(log2((double)K / i));
		ans += (double)pow(0.5, logk);
	}

	printf("%.12lf\n", ans / N);
	// cout << ans << endl;
	return 0;
}
