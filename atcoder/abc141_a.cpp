// https://atcoder.jp/contests/abc141/tasks/abc141_a
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

    string ans;
    if (S == "Sunny")  ans = "Cloudy";
    if (S == "Cloudy") ans = "Rainy";
    if (S == "Rainy")  ans = "Sunny";

	cout << ans << endl;
	return 0;
}
