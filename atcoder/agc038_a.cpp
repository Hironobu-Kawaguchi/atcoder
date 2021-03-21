// https://atcoder.jp/contests/agc038/tasks/agc038_a
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
// #include<set>
// #include<queue>
// #include<deque>
// #include<regex>
// #include<bitset>
// #include<iomanip>
// #include<complex>
// #include<stack>
// #include<functional>

#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int h, w, a, b;
	cin >> h >> w >> a >> b;
    string ans = "";
    vector<vector<char>> s(h, vector<char>(w, '0'));
    rep(i, h) {
        rep(j, w) {
            if ((i<b && j<a) || (i>=b && j>=a)) {
                s[i][j] = '1';
            }
        }
    }
    // if (a==b) {
    //     int k = 0;
    //     rep(i, h) {
    //         rep(j, a) {
    //             if (k+j >= w) k=-j;
    //             s[i][k+j] = '1';
    //         }
    //         k += a;
    //     }
    // } else if (a==0) {
    //     rep(i, h) {
    //         if (i>=b) break;
    //         rep(j, w) {
    //             s[i][j] = '1';
    //         }
    //     }
    // } else if (b==0) {
    //     rep(i, h) {
    //         rep(j, w) {
    //             if (j>=a) break;
    //             s[i][j] = '1';
    //         }
    //     }
    // } else {
    //     rep(i, h) {
    //         rep(j, w) {
    //             if ((i<b && j<a) || (i>=b && j>=a)) {
    //                 s[i][j] = '1';
    //             }
    //         }
    //     }
    // } 

    rep(i, h) {
        ans = "";
        rep(j, w) {
            ans += s[i][j];
        }
        cout << ans << endl;
    }

	return 0;
}
