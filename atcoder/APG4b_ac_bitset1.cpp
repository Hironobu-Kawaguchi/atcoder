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
	bitset<8> a("00011011");
	bitset<8> b("00110101");

	auto c = a & b;
	cout << "1: " << c << endl;         // 1: 00010001
	cout << "2: " << (c << 1) << endl;  // 2: 00100010
	cout << "3: " << (c << 2) << endl;  // 3: 01000100
	cout << "4: " << (c << 3) << endl;  // 4: 10001000
	cout << "5: " << (c << 4) << endl;  // 5: 00010000

	c <<= 4;
	c ^= bitset<8>("11010000"); // XOR演算の複合代入演算子
	cout << "6: " << c << endl; // 6: 11000000

	bitset<4> S;
	S.set(0, 1);  // 0番目のビットを1にする
	cout << S << endl;

	if (S.test(3)) {
		cout << "4th bit is 1" << endl;
	}
	else {
		cout << "4th bit is 0" << endl;
	}

	int x = 0b0101;
	int y = 0b1010;
	//if (x & y > 0) { // &演算子よりも>演算子の優先度の方が高いので x & (y > 0) と解釈される
	if ((x & y) > 0) {
		cout << "yes" << endl;
	}
	else {
		cout << "no" << endl;
	}

	// 3ビットのビット列をすべて列挙する
	for (int tmp = 0; tmp < (1 << 3); tmp++) {
		bitset<3> s(tmp);
		// ビット列を出力
		cout << s << endl;
	}

	return 0;
}
