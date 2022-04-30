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

long long N;
long long A[1 << 18], B[1 << 18];
bool used[1 << 18];

void Solve() {
	// Step #1. Input
	cin >> N;

	// Step #2. Decide Integers
	for (int i = 0; i < 18; i++) used[1 << i] = true;
	for (int i = 0; i < 30; i++) A[i] = (1LL << i);
	int cur = 1;
	for (int i = 30; i < 100; i++) {
		while (used[cur] == true) cur += 1;
		A[i] = cur; cur += 1;
	}
	for (int i = 0; i < N; i++) {
		if (i) cout << " ";
		cout << A[i];
	}
	cout << endl;

	// Step #3. Input 2 & Get Sum
	long long Goal = 0;
	for (int i = 0; i < N; i++) cin >> B[i];
	for (int i = 0; i < N; i++) Goal += B[i];
	for (int i = 0; i < N; i++) Goal += A[i];
	Goal /= 2LL;

	// Step #4. Output
	vector<long long> vec;
	for (int i = 0; i < N; i++) {
		if (Goal >= B[i]) { Goal -= B[i]; vec.push_back(B[i]); }
	}
	for (int i = 29; i >= 0; i--) {
		if (Goal >= A[i]) { Goal -= A[i]; vec.push_back(A[i]); }
	}
	for (int i = 0; i < (int)vec.size(); i++) {
		if (i) cout << " ";
		cout << vec[i];
	}
	cout << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		Solve();
	}
	return 0;
}