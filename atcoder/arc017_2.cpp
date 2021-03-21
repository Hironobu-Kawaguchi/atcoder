// https://atcoder.jp/contests/arc017/tasks/arc017_2
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
	int N, K;
	cin >> N >> K;
    int ans = 0;
    vector<int> A(N);
    int cnt = 1;
    rep(i,N) {
        cin >> A[i];
        if(i) {
            if(A[i-1] < A[i]) cnt++;
            else {
                ans += max(0, cnt-K+1);
                cnt = 1;
            }
        }
    } 
    ans += max(0, cnt-K+1);
	cout << ans << endl;
	return 0;
}
