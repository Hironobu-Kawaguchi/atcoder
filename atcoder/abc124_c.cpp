// C - Coloring Colorfully
// https://atcoder.jp/contests/abc124/tasks/abc124_c

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	string S;
	cin >> S;

	//初期値は大きい値
	int ans = S.size();

	//iは最初に使う色（0 or 1）
	for (int i = 0; i < 2; i++)
	{
		// iを最初に使う時に変えなければならないタイルの数
		int cnt = 0;

		for (int j = 0; j < S.size(); j++)
		{
			// (char)(0 + '0') -> '0';
			// (char)(1 + '0') -> '1';
			if ((j % 2 == 0) ^ (S[j] != (char)(i + '0'))) cnt++;
		}

		ans = min(ans, cnt);
	}

	cout << ans << endl;
	return 0;
}

// #include <iostream>
// #include <algorithm>
// #include <string>
// #include <vector>
// #include <tuple>
// #include <queue>
// // #include <bits/stdc++.h>
// using namespace std;

// int main() {
// 	string S;
// 	cin >> S;

// 	int N = S.size();
// 	int even0odd1 = 0, odd0even1 = 0;

// 	for (int i = 0; i < N; i++) {
// 		if (i % 2 == 0) {
// 			if (S.at(i) == '0')	even0odd1++;
// 			else                odd0even1++;
// 		}
// 		else {
// 			if (S.at(i) == '1')	even0odd1++;
// 			else                odd0even1++;
// 		}
// 	}

// 	cout << min(even0odd1, odd0even1) << endl;
// 	return 0;
// }
