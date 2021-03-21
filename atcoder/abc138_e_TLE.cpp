// https://atcoder.jp/contests/abc138/tasks/abc138_e
#include<iostream>
#include<algorithm>
//#include <numeric>
#include<string>
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
	string s, t;
	cin >> s >> t;

	int slen = s.size();
	int tlen = t.size();
	int i = 0;	// sの文字番号
	int j = 0;	// tの文字番号
	int k = 0;  // sから探した文字数
	ll ans = 0;


	while (j < tlen) {
		if (s[i] == t[j]) {
			if (i < slen-1) i++; else i = 0;
			ans++;
			j++;
			k = 0;
		}
		else {
			if (i < slen-1) i++; else i = 0;
			ans++;
			k++;
			if (k > slen + 1) {
				ans = -1;
				j = tlen;
				break;
			}
		}
	}

	cout << ans << endl;

	return 0;
}
