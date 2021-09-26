// https://atcoder.jp/contests/genocon2021/tasks/genocon2021_c
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
// #include <atcoder/all>
// using namespace atcoder;
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

clock_t start = clock();
const int MAX_M = 40;
int m;
vector<string> s(MAX_M);

void pairwise_alignment(int si, int ti, bool sadd_flag=true) {
    int sn = s[si].size(), tn = s[ti].size();
    vector<vector<int>> dp(sn+1, vector<int>(tn+1, -INF));
    dp[0][0] = 0;
    vector<vector<int>> from(sn+1, vector<int>(tn+1));
    rep(i,sn+1) rep(j,tn+1) {
        if (i!=0) {
            if (dp[i][j] < dp[i-1][j] - 1) {
                dp[i][j] = dp[i-1][j] - 1;
                from[i][j] = 0;
            }
        }
        if ((j!=0) && (sadd_flag)) {
            if (dp[i][j] < dp[i][j-1] - 1) {
                dp[i][j] = dp[i][j-1] - 1;
                from[i][j] = 1;
            }
        }
        if ((i!=0) && (j!=0)) {
            if (s[si][i-1]==s[ti][j-1]) {
                if (dp[i][j] < dp[i-1][j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                    from[i][j] = 2;
                }
            } else {
                if (dp[i][j] < dp[i-1][j-1] - 1) {
                    dp[i][j] = dp[i-1][j-1] - 1;
                    from[i][j] = 2;
                }
            }
        }
    }
    string ress, rest;
    int i = sn, j = tn;
    while ((i>0) || (j>0)) {
        if (from[i][j]==2) {
            ress += s[si][i-1];
            rest += s[ti][j-1];
            i--; j--;
        } else if (from[i][j]==0) {
            ress += s[si][i-1];
            rest += '-';
            i--;
        } else {
            ress += '-';
            rest += s[ti][j-1];
            j--;
        }
    }
    reverse(ress.begin(), ress.end());
    reverse(rest.begin(), rest.end());
    s[si] = ress;
    s[ti] = rest;
    return;
}

int get_score() {
    int n = s[0].size();
    int cs = 0;
    rep(i,n) {
        vector<int> cnt(5);
        rep(j,m) {
            if(s[j][i]=='-')      cnt[0]++;
            else if(s[j][i]=='A') cnt[1]++;
            else if(s[j][i]=='C') cnt[2]++;
            else if(s[j][i]=='G') cnt[3]++;
            else if(s[j][i]=='T') cnt[4]++;
        }
        sort(cnt.rbegin(), cnt.rend());
        cs += cnt[1];
    }
    return cs;
}


int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	cin >> m;
    rep(i,m) cin >> s[i];
    vector<string> s_origin(MAX_M);
    copy(s.begin(), s.end(), s_origin.begin());

    int score_best = INF;
    vector<string> s_best(MAX_M);
    rep(k,m) {
        copy(s_origin.begin(), s_origin.end(), s.begin());
        rep(i,m) if(i!=k) pairwise_alignment(k, i, true);
        rep(i,m) if(i!=k) pairwise_alignment(k, i, false);
        int score = get_score();
        if (score<score_best) {
            score_best = score;
            copy(s.begin(), s.end(), s_best.begin());
        }
        if (1000.0 * (clock() - start) / CLOCKS_PER_SEC > 9000) break;
    }
    rep(i,m) cout << s_best[i] << "\n";
	return 0;
}
