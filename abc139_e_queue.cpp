// https://atcoder.jp/contests/abc139/tasks/abc139_e
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
ll gcd(ll a, ll b) { return b?gcd(b,a%b):a;}
ll lcm(ll a, ll b) { return a/gcd(a,b)*b;}

int main() {
    int n;
    cin >> n;
    vector<vector<int>> a(n, vector<int>(n-1));
    rep(i,n) {
        rep(j,n-1) {
            cin >> a[i][j];
            a[i][j]--;
        }
        reverse(a[i].begin(), a[i].end());  // vectorは末尾のアクセスが早いのでreverseしておく
    }
    vector<P> q;
    auto check = [&](int i) {   // ラムダ式 iと試合できるペアをqに入れる
        if (a[i].size() == 0) return;
        int j = a[i].back();    // j: 対戦相手（末尾）
        if (a[j].size() == 0) return;
        if (a[j].back() == i) { // 対戦できる場合
            P p(i,j);
            if (p.second < p.first) swap(p.first, p.second);
            q.push_back(p);
        }
    };
    rep(i,n) {
        check(i);
    }
    int day = 0;
    while (q.size() > 0) {
        day++;
        sort(q.begin(), q.end());
        q.erase(unique(q.begin(), q.end()), q.end());   // 重複を削除
        vector<P> prevQ;
        swap(prevQ, q);
        for (P p : prevQ) {
            int i = p.first, j = p.second;
            a[i].pop_back();
            a[j].pop_back();
        }
        for (P p : prevQ) {
            int i = p.first, j = p.second;
            check(i);
            check(j);
        }
    }
    rep(i,n) {
        if (a[i].size() != 0) {     // 試合が残ってたら-1
            puts("-1");
            return 0;
        }
    }
    cout << day << endl;
    return 0;
}
