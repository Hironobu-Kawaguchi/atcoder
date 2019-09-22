// https://atcoder.jp/contests/abc119/tasks/abc119_c
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

int n;
vector<int> abc(3); // A, B, C を配列で持つことで、ループ処理を可能にする
int ans = INF;
vector<P> now(4, P(0, 0));  // 長さの合計、使用本数をpairで持つ

void dfs(int depth, vector<int> &l) {
    if (depth == n) {
        int tmp = 0;
        rep(i, 3) {
            if (now[i].second == 0) return;
            // 目的の長さとの差 + 合成魔法で使ったMP
            tmp += abs(abc[i] - now[i].first) + 10 * (now[i].second - 1);
        }
        ans = min(ans, tmp);
        return;
    }
    rep(i, 4) { // 各竹は4つのグループ(A,B,C,未使用)に入る可能性がある
        now[i].first += l[depth];
        now[i].second += 1;
        dfs(depth + 1, l);
        now[i].first -= l[depth];   // 抜けたら選択を戻す
        now[i].second -= 1;
    }
}

int main() {
	cin >> n;
    rep(i, 3) cin >> abc[i];
    vector<int> l(n);
    rep(i, n) cin >> l[i];
    dfs(0, l);
	cout << ans << endl;
	return 0;
}
