// https://atcoder.jp/contests/abc159/tasks/abc159_e
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
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

int main() {
	int h, w, k;
	cin >> h >> w >> k;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    int ans = INF;
    rep(div,1<<(h-1)) {     // 2**(h-1)パターンの横分割を全探索
        int g = 0;          // 横分割されるgroup数
        vector<int> id(h);  // 各行がどのgroupに入るか
        rep(i,h) {
            id[i] = g;
            if (div>>i&1) ++g;
        }
        ++g;
        vector<vector<int>> c(g, vector<int>(w));   // group毎の白の数
        rep(i,h)rep(j,w) c[id[i]][j] += (s[i][j]-'0');

        int num = g-1;
        vector<int> now(g); // group毎の白の累計
        auto add = [&](int j) {
            rep(i,g) now[i] += c[i][j];
            rep(i,g) if(now[i] > k) return false;
            return true;
        };
        rep(j,w) {
            if (!add(j)) {  // これまでの累計に加算してkを超えた場合
                num++;      // 縦に分割
                now = vector<int>(g);   // nowを初期化
                if (!add(j)) {          // nowを初期化後、1列だけでk以上の時はダメ
                    num = INF;
                    break;
                }
            }
        }
        ans = min(ans, num);
    }
	cout << ans << endl;
	return 0;
}
