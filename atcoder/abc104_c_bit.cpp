// https://atcoder.jp/contests/abc104/tasks/abc104_c
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
#define all(v) (v).begin(),(v).end()
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int D, G;
	cin >> D >> G;
    vector<int> p(D), c(D);
    rep(i, D) cin >> p[i] >> c[i];

    int ans = INF;
    for (int s = 0; s < (1<<D); s++) {
        int solve = 0, score = 0;
        int partial = -1;
        rep(i, D) {
            // i番目のセットをすべて解く
            if (s & (1<<i)) {
                solve += p[i];
                score += 100*(i+1)*p[i] + c[i];
            } else {
                // 余ったセットで最高点のもの
                partial = i;
            }
        }
        // G点に達するまで問題を解く
        int less = G - score;
        if (less > 0) {
            int prob_score = 100*(partial+1);    // 余ったセットで最高点の1問の点数
            // 解ききっても足りないなら、その組み合わせは不適
            if (less > prob_score*p[partial]) continue;
            // fllor(less/(1問あたらいの点数))
            solve += min(p[partial], (less + (prob_score - 1))/prob_score);
        }
        ans = min(ans, solve);
    }
	cout << ans << endl;
	return 0;
}
