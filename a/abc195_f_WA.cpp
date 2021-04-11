// https://atcoder.jp/contests/abc195/tasks/abc195_f
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
// #include <atcoder/all>
// using namespace atcoder;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define drep(i,n) for(int i = (n-1); i >= 0; i--)
#define all(v) (v).begin(),(v).end()
#define maxs(x,y) (x = max(x,y))
#define mins(x,y) (x = min(x,y))
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template <class T> T lcm(T a, T b) { return a/gcd(a,b)*b; }
typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

// i ~ N-1の範囲にNの約数が存在するか
bool has_divisor(int N, int i) {
	// ベースケース1
	if (i == N - 1) {
		return (N % i == 0);
	}
	// ベースケース2
	if (N % i == 0) {
		// 実際にiはNの約数なので、i ~ N-1の範囲に約数が存在する
		return true;
	}

	// 再帰ステップ
	// i+1 ~ N-1の範囲の結果がi ~ N-1の範囲の結果となる
	// (ベースケース2によって、iがNの約数の場合は取り除かれているので、あとはi+1 ~ N-1の範囲を調べればよい)
	return has_divisor(N, i + 1);
}

bool is_prime(int N) {
	if (N == 1) {
		// 1は素数ではない
		return false;
	}
	else if (N == 2) {
		// 2は素数
		return true;
	}
	else {
		// 2~(N-1)の範囲に約数が無ければ、Nは素数
		return !has_divisor(N, 2);
	}
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    ll a, b;
	cin >> a >> b;
    vector<ll> yakusu(b-a+1, 1);
    for (int i = 2; i < 73; i++) {
        if (!is_prime(i)) continue;
        for (ll x = a; x <= b; x++) {
            if (x%i==0) yakusu[x-a] *= i;
        }
    }
    rep(i,b-a+1) cout << yakusu[i] << endl;
    // ll ans = 0;
	// cout << ans << endl;
	return 0;
}

