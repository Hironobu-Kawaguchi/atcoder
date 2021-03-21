// https://atcoder.jp/contests/abc141/tasks/abc141_c
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
    int N, K, Q;
	cin >> N >> K >> Q;
    vector<int> A(Q), cnt(N);
    rep(i, Q) {
        cin >> A[i];
        cnt[A[i]-1]++;
    }
    rep(i, N) {
        if (K-Q+cnt[i] > 0) cout << "Yes" << endl;
        else                cout << "No" << endl;
    }

	return 0;
}
