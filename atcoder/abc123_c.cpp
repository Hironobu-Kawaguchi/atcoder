// C - Five Transportations
// https://atcoder.jp/contests/abc123/tasks/abc123_c

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;


int main() {
	long long N;
	long long A, B, C, D, E;
	cin >> N;
	cin >> A >> B >> C >> D >> E;

	long long MinMove = min({ A,B,C,D,E });

	long long ans = ((N + MinMove - 1) / MinMove) + 4;

	cout << ans << endl;
}
