// https://atcoder.jp/contests/abc129/tasks/abc129_d
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
	int H, W;
	cin >> H >> W;
    vector<string> S(H);
    rep(i, H) cin >> S[i];
    vector<vector<int>> cnt(H, vector<int>(W));
    rep(i, H) {
        vector<int> done(W);
        rep(j, W) {
            if (S[i][j] == '#') continue;
            if (done[j]) continue;
            int l = 0;
            while (j+l < W) {
                if (S[i][j+l] == '#') break;
                ++l;
            } 
            rep(k,l) {
                cnt[i][j+k] += l;
                done[j+k] = 1;
            }
        }
    }
    rep(j, W) {
        vector<int> done(H);
        rep(i, H) {
            if (S[i][j] == '#') continue;
            if (done[i]) continue;
            int l = 0;
            while (i+l < H) {
                if (S[i+l][j] == '#') break;
                ++l;
            } 
            rep(k,l) {
                cnt[i+k][j] += l;
                done[i+k] = 1;
            }
        }
    }
    int ans = 0;
    rep(i,H)rep(j,W) ans = max(ans, cnt[i][j]-1);
	cout << ans << endl;
	return 0;
}
