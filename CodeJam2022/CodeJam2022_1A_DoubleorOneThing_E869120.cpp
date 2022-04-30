#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

void Solve(int TestNum) {
	// Input
	string S, T = "";
	cin >> S;

	// Tansaku
	for (int i = 0; i < S.size(); i++) {
		int cur = (int)(S[i]), nex = 0;
		for (int j = i + 1; j < S.size(); j++) {
			if (S[i] != S[j]) { nex = (int)(S[j]); break; }
		}
		if (cur < nex) { T += S[i]; T += S[i]; }
		else { T += S[i]; }
	}

	// Output
	cout << "Case #" << TestNum << ": " << T << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		Solve(i);
	}
	return 0;
}