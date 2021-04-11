// https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
#include <iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
#include<vector>
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
// #include<bits/stdc++.h>

using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
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
    int t;
    cin >> t;
    for (int x = 1; x <= t; ++x) {
        int X, Y;
        string S;
        cin >> X >> Y >> S;
        int n = S.size();
        vector<vector<int>> dp(n, vector<int>(4,INF));  // 0:CC, 1:CJ, 2:JC, 3:JJ
        if (S[0]=='C') {
            dp[0][0] = 0, dp[0][2] = 0;
        } else if (S[0]=='J') {
            dp[0][1] = 0, dp[0][3] = 0;
        } else {  // '?'
            dp[0][0] = 0, dp[0][1] = 0, dp[0][2] = 0, dp[0][3] = 0;
        }
        rep(i,n-1) {
            if (S[i]=='C') {
                if (S[i+1]=='C') {
                    dp[i+1][0] = min(dp[i][0], dp[i][2]);
                } else if (S[i+1]=='J') {
                    dp[i+1][1] = min(dp[i][0], dp[i][2]) + X;
                } else {  // '?'
                    dp[i+1][0] = min(dp[i][0], dp[i][2]);
                    dp[i+1][1] = min(dp[i][0], dp[i][2]) + X;
                }
            } else if (S[i]=='J') {
                if (S[i+1]=='C') {
                    dp[i+1][2] = min(dp[i][1], dp[i][3]) + Y;
                } else if (S[i+1]=='J') {
                    dp[i+1][3] = min(dp[i][1], dp[i][3]);
                } else {  // '?'
                    dp[i+1][2] = min(dp[i][1], dp[i][3]) + Y;
                    dp[i+1][3] = min(dp[i][1], dp[i][3]);
                }
            } else {  // '?'
                if (S[i+1]=='C') {
                    dp[i+1][0] = min(dp[i][0], dp[i][2]);
                    dp[i+1][2] = min(dp[i][1], dp[i][3]) + Y;
                } else if (S[i+1]=='J') {
                    dp[i+1][1] = min(dp[i][0], dp[i][2]) + X;
                    dp[i+1][3] = min(dp[i][1], dp[i][3]);
                } else {  // '?'
                    dp[i+1][0] = min(dp[i][0], dp[i][2]);
                    dp[i+1][2] = min(dp[i][1], dp[i][3]) + Y;
                    dp[i+1][1] = min(dp[i][0], dp[i][2]) + X;
                    dp[i+1][3] = min(dp[i][1], dp[i][3]);
                }
            }
        }
        int y = INF;
        rep(i,4) y = min(y, dp[n-1][i]);
        cout << "Case #" << x << ": " << y << endl;
    }
    return 0;
}
