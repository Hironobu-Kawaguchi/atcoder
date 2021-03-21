// https://atcoder.jp/contests/abc116/tasks/abc116_d
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
    int n, k;
    cin >> n >> k;
    vector<vector<int>> ds(n);  // ネタの種類t(<=n)別においしさdのリスト
    rep(i,n) {
        int t, d;
        cin >> t >> d;
        --t;
        ds[t].push_back(d);
    }

    vector<int> y0, y1;
    rep(i,n) {
        if (ds[i].size() == 0) continue;
        sort(ds[i].begin(), ds[i].end());   // 各ネタでおいしさのsort
        y1.push_back(ds[i].back());         // 各ネタで最大のおいしさをpopしy1に追加
        ds[i].pop_back();
        y0.insert(y0.end(), ds[i].begin(), ds[i].end());    // 各ネタで2番目以降のおいしさのリストをy0に追加
    }
    sort(y0.rbegin(), y0.rend());   // ネタの種類が増えないおいしさのリスト（各ネタで2番目以降）を降順sort
    sort(y1.rbegin(), y1.rend());   // ネタの種類が増えるおいしさ（各ネタで最大）のリストを降順sort

    ll ans = 0;
    // int Y = max(0, k-int(y0.size()));   // Y: ネタの種類の最小値（kまで増やしながら貪欲するため）
    int Y = min(k, int(y1.size()));   // Y: ネタの種類の最大値（減らしながら貪欲するため）
    ll X = 0;
    rep(i,Y) X += y1[i];    // Y個 ネタの種類が増えるおいしさ（各ネタで最大）を大きい順に加算
    rep(i,k-Y) X += y0[i];  // k-Y個 ネタの種類が増えないおいしさを大きい順に加算
    while (1) {
        ans = max(ans, X + (ll)Y*Y);
        // if (Y >= k || Y >= y1.size()) break;    // Yをkまで増やしながら貪欲
        // X += y1[Y];     // ネタの種類が増えるおいしさ（各ネタで最大）を大きい順に1つ追加
        // X -= y0[k-Y-1]; // ネタの種類が増えない大きさを小さい順に1つ除外
        // ++Y;
        if (Y <= 0 || k-Y >= y0.size()) break;    // Yを減らしながら貪欲
        X -= y1[Y-1];     // ネタの種類が増えるおいしさ（各ネタで最大）を小さい順に1つ除外
        X += y0[k-Y]; // ネタの種類が増えない大きさを大きい順に1つ追加
        --Y;
    }
    cout << ans << endl;
    return 0;
}
