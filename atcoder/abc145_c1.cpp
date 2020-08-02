// https://atcoder.jp/contests/abc145/tasks/abc145_c
// https://atcoder.jp/contests/abc145/submissions/8474526
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

int N;
vector<int> x(10), y(10);

double dist(int i, int j) {
    double dx = x[i] - x[j];
    double dy = y[i] - y[j];
    return pow(dx * dx + dy * dy, 0.5);
}

int main() {
    cin >> N;
    rep(i, N) cin >> x[i] >> y[i];
    double sum = 0.0;

    vector<int> v(N);
    rep(i, N) v[i] = i;
    do {
        rep(i, N-1) sum += dist(v[i], v[i+1]);
    } while(next_permutation(v.begin(), v.end()));

    int Factorial = 1;
    for (int i = 2; i <= N; i++) Factorial *= i;

    cout << fixed << setprecision(10) << sum / Factorial << endl;
	return 0;
}
