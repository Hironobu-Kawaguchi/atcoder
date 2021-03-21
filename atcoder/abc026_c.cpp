// https://atcoder.jp/contests/abc026/tasks/abc026_c
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
#define chmin(x,y) x = min(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int N;
	cin >> N;
    vector<vector<int>> sub(N);
    int b;
    rep(i, N-1) {
        cin >> b;
        sub[b-1].push_back(i+1);
    }

    vector<int> P(N), maxP(N), minP(N);
    for (int i = N-1; i >= 0; i--) {
        if (sub[i].size()==0) {
            P[i] = 1;
            continue;
        }
        maxP[i] = 0;
        minP[i] = (int)1e9;
        for (int j: sub[i]) {
            maxP[i] = max(maxP[i], P[j]);
            minP[i] = min(minP[i], P[j]);
        }
        P[i] = maxP[i] + minP[i] + 1;
    }
	cout << P[0] << endl;
	return 0;
}
