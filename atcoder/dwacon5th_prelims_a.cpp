// https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_a
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
    vector<int> a(N);
    int sm = 0;
    rep(i,N) {
        cin >> a[i];
        sm += a[i];
    }
    float avg = (float) sm / N;
    float mn = 100;
    vector<float> dif(N);
    rep(i,N) {
        dif[i] = (float) abs(a[i] - avg);
        mn = min(mn, dif[i]);
    } 
    int ans;
    rep(i,N) {
        if (dif[i] == mn) {
            ans = i;
            break;
        }
    }
	cout << ans << endl;
	return 0;
}
