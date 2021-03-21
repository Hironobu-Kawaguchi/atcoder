// https://atcoder.jp/contests/abc104/tasks/abc104_c
#include<iostream>
// #include<algorithm>
// #include<string>
#include<numeric>
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
    vector<int> v(D);
    iota(all(v), 0);

    int ans = INF;
    while (true) {
        int solve = 0, score = 0;
        for (auto i : v) {
            if (score + 100*(i+1)*p[i] + c[i] <= G) {
                solve += p[i];
                score += 100*(i+1)*p[i] + c[i];
            } else {
                int less = G - score;
                if (less == 0) break;
                solve += min(p[i], (less - 1)/(100*(i+1)) + 1);
                break;
            }
        }        
        ans = min(ans, solve);
        if (!next_permutation(all(v))) break;
    }
	cout << ans << endl;
	return 0;
}
