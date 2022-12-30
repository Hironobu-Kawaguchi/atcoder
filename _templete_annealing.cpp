// https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_at
#include<iostream>
// #include<algorithm>
// #include<cmath>
// #include<ctime>
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
// typedef pair<int, int> P;
typedef long long ll;
const int INF = 1001001001;
const ll LINF = 1001002003004005006ll;
const ll MOD = 1e9+7;

const int MAX_N = 159;
int N, X[MAX_N], Y[MAX_N];
int P[MAX_N]; // 都市を訪れる順番の情報

// 都市 p と q の間の距離を求める関数
double GetDistance(int p, int q) {
    return sqrt((X[p] - X[q]) * (X[p] - X[q]) + (Y[p] - Y[q]) * (Y[p] - Y[q]));
}

// a 以上 b 以下の整数をランダムに返す関数
int RandInt(int a, int b) {
    return a + rand() % (b - a + 1);
}

// 0 以上 1 以下のランダムな実数を返す関数
double Randouble() {
	return 1.0 * rand() / RAND_MAX;
}

// スコアを計算する関数
double GetScore() {
    double sum = 0;
    for (int i = 1; i <= N; i++) sum += GetDistance(P[i], P[i+1]);
    return sum;
}

int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
	// 入力
	cin >> N;
    for (int i = 1; i <= N; i++) cin >> X[i] >> Y[i];

	// 初期解生成
    P[1] = 1; P[N+1] = 1;
    for (int i = 2; i <= N; i++) P[i] = i;

	// 焼きなまし法（GetScore 関数、RandInt 関数は 7.2 節を参照）
    double CurrentScore = GetScore();
    for (int t = 1; t <= 200000; t++) {
		// ランダムに反転させる区間 [L, R] を選ぶ
        int L = RandInt(2, N);
        int R = RandInt(2, N);
        if (L > R) swap(L, R);

        // reverse は配列の L ～ R 番目を反転させる関数
        reverse(P + L, P + R + 1);
        double NewScore = GetScore();

		// 7.2 節の解答例から変更した唯一の部分（Probability は採用確率）
        double T = 30.0 - 28.0 * t / 200000.0;
        double Probability = exp(min(0.0, (CurrentScore - NewScore) / T));
        if (Randouble() <= Probability) CurrentScore = NewScore;
        else reverse(P + L, P + R + 1);
    }

	// 出力
    for (int i = 1; i <= N + 1; i++) cout << P[i] << endl;

	return 0;
}
