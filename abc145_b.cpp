// https://atcoder.jp/contests/abc145/tasks/abc145_b
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
    string S;
    cin >> S;

    int K = N /2;
    if (N%2 == 0 && S.substr(0, K) == S.substr(K, K)) {
        cout << "Yes" << endl;
    } else {
        cout << "No"  << endl;
    }

	return 0;
}
