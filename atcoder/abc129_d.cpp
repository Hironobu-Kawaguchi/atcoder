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

#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int h, w;
	cin >> h >> w;
    vector<string> s(h+2);
    s[0] = string(w+2, '#');
    s[h+1] = string(w+2, '#');
    rep(i,h) {
        string sin;
        cin >> sin;
        s[i+1] = '#' + sin + '#';
    }
    // rep(i,h+2) cout << s[i] << endl;

    vector<vector<int>> yoko(h+2, vector<int>(w+2)), tate(h+2, vector<int>(w+2));
    rep(i,h+2) {
        int start = 0, end = 0;
        rep(j,w+2) {
            if(s[i][j] == '#') {
                int num = end - start;
                if(num) {
                    for (int k = start; k < end; k++) {
                        yoko[i][k] = num;
                    }
                }
                start = j+1; end = j+1;
            }
            else {
                end++;
            }
        }
    }
    rep(j,w+2) {
        int start = 0, end = 0;
        rep(i,h+2) {
            if(s[i][j] == '#') {
                int num = end - start;
                if(num) {
                    for (int k = start; k < end; k++) {
                        tate[k][j] = num;
                    }
                }
                start = i+1; end = i+1;
            }
            else {
                end++;
            }
        }
    }
    // rep(i,h+2) {
    //     rep(j,w+2) {
    //         cout << tate[i][j];
    //     }
    //     cout << endl;
    // }
    // rep(i,h+2) {
    //     rep(j,w+2) {
    //         cout << yoko[i][j];
    //     }
    //     cout << endl;
    // }

    int ans = 0;
    rep(i,h+2) rep(j,w+1){
        ans = max(ans, tate[i][j] + yoko[i][j] - 1);
    }
	cout << ans << endl;
	return 0;
}



// #include <bits/stdc++.h>
// #define rep(i,n) for (int i = 0; i < (n); ++i)
// using namespace std;
// typedef long long ll;

// int main() {
// 	int H, W;
// 	cin >> H >> W;
//     vector<string> S(H);
//     rep(i, H) cin >> S[i];
//     vector<vector<int>> cnt(H, vector<int>(W));
//     rep(i, H) {
//         vector<int> done(W);
//         rep(j, W) {
//             if (S[i][j] == '#') continue;
//             if (done[j]) continue;
//             int l = 0;
//             while (j+l < W) {
//                 if (S[i][j+l] == '#') break;
//                 ++l;
//             } 
//             rep(k,l) {
//                 cnt[i][j+k] += l;
//                 done[j+k] = 1;
//             }
//         }
//     }
//     rep(j, W) {
//         vector<int> done(H);
//         rep(i, H) {
//             if (S[i][j] == '#') continue;
//             if (done[i]) continue;
//             int l = 0;
//             while (i+l < H) {
//                 if (S[i+l][j] == '#') break;
//                 ++l;
//             } 
//             rep(k,l) {
//                 cnt[i+k][j] += l;
//                 done[i+k] = 1;
//             }
//         }
//     }
//     int ans = 0;
//     rep(i,H)rep(j,W) ans = max(ans, cnt[i][j]-1);
// 	cout << ans << endl;
// 	return 0;
// }
