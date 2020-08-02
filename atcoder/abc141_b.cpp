// https://atcoder.jp/contests/abc141/tasks/abc141_b
#include<iostream>
// #include<algorithm>
// #include<string>
// #include <numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
// #include<queue>
// #include<regex>
// #include <bitset>

#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
    string S;
	cin >> S;

    string ans = "Yes";
    rep(i, S.size()) {
        if (i%2 == 0 && S.at(i) == 'L') ans = "No";
        if (i%2 == 1 && S.at(i) == 'R') ans = "No";
    }
	cout << ans << endl;
	return 0;
}
