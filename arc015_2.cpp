// https://atcoder.jp/contests/arc015/tasks/arc015_2
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
#define chmax(x,y) x = max(x,y)
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int N;
	cin >> N;
    vector<int> ans(6, 0);
    double mxt, mnt;
    rep(i,N) {
        cin >> mxt >> mnt;
        if (mxt >= 35.0)      ans[0]++;
        else if (mxt >= 30.0) ans[1]++;
        else if (mxt >= 25.0) ans[2]++;
        else if (mxt < 0.0)   ans[5]++;
        if (mnt >= 25.0)      ans[3]++;
        else if (mnt < 0 and mxt >= 0) ans[4]++;
    }
	rep(i,6) {
        if (i) cout <<' ';
        cout << ans[i];
    }
    cout << endl;
	return 0;
}
