// https://atcoder.jp/contests/abc030/tasks/abc030_a
#include<iostream>
#include<algorithm>
//#include <numeric>
//#include<string>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;


int main() {
	// 入力
	int A, B, C, D;
	cin >> A >> B >> C >> D;

	double AB, CD;
	AB = (double)B / A;
	CD = (double)D / C;
	if (AB == CD) {
		cout << "DRAW" << endl;
	} else if (AB > CD) {
		cout << "TAKAHASHI" << endl;
	} else {
		cout << "AOKI" << endl;
	}

	return 0;
}
