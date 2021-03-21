// https://atcoder.jp/contests/abc141/tasks/abc141_d
#include<iostream>
// #include<algorithm>
// #include<string>
// #include <numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
#include<queue>
// #include<regex>
// #include <bitset>

#include <bits/stdc++.h>
#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long ll;

int main() {
    int N, M;
	cin >> N >> M;
    priority_queue<int> q;
    rep(i, N) {
        int A;
        cin >> A;
        q.push(A);
    }
    rep(i, M) {
        int a = q.top(); q.pop();
        q.push(a/2);
    }
    ll ans = 0;
    rep(i, N) {
        ans += q.top(); q.pop();
    }
    cout << ans << endl;
	return 0;
}
