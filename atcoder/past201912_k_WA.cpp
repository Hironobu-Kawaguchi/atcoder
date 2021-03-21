// https://atcoder.jp/contests/past201912/tasks/past201912_k
#include<iostream>
// #include<algorithm>
// #include<string>
// #include<numeric>
// #include<vector>
// #include<map>
// #include<tuple>
#include<set>
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

vector<set<int>> sub(150010);

int dfs(int a, set<int> s) {
    if (sub[a].empty()) return 0;
    for (int j: sub[a]) {
        for (int b: s)  sub[b].insert(j);
        s.insert(a);
        dfs(j, s);
        // for (int k: sub[j]) {
        //     sub[b].insert(k);
        // }
    }
    return 0;
}

int main() {
	int N;
	cin >> N;
    // vector<set<int>> sub(N);
    vector<int> p(N);
    int boss;
    rep(i, N) {
        cin >> p[i];
        if (p[i] == -1) boss = i;
        else sub[p[i]-1].insert(i);
    }
    set<int> s;
    s.insert(boss);
    dfs(boss, s);

    int Q;
    cin >> Q;
    rep(i, Q) {
        int a, b;
        cin >> a >> b;
        if (p[b-1] == -1)             cout << "Yes" << endl;
        else if (sub[b-1].count(a-1)) cout << "Yes" << endl;
        else                          cout << "No"  << endl;
        // for (int j : sub[b-1]) {
        //     cout << j+1 << ' ';
        // }
        // cout << endl;
    }
	return 0;
}
