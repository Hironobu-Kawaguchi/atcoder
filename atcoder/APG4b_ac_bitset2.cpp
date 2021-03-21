// https://atcoder.jp/contests/apg4b/tasks/APG4b_ac
#include<iostream>
#include<algorithm>
//#include<string>
//#include <numeric>
//#include<vector>
//#include<map>
//#include<tuple>
//#include<set>
//#include<queue>
//#include<regex>
#include <bitset>

// #include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
	uint32_t x = 0b100;
	cout << x << endl;  // 4

	cout << (x | 0b010) << endl;  // 計算結果は 0b110 = 6

	return 0;
}
