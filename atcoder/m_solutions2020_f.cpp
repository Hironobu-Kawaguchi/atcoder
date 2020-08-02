// https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_f
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

int N, X[1 << 18], Y[1 << 18];
char D[1 << 18];

void Rotate() {
    // 時計回りに90度回転
	for (int i = 1; i <= N; i++) {
		int cx = Y[i], cy = 200000 - X[i];
        char cz;
		if (D[i] == 'U') cz = 'R';
		if (D[i] == 'R') cz = 'D';
		if (D[i] == 'D') cz = 'L';
		if (D[i] == 'L') cz = 'U';
		X[i] = cx; Y[i] = cy; D[i] = cz;
	}
}

vector<pair<int, char>> V1[1 << 19];
vector<pair<int, char>> V2[1 << 19];

int solve_01() {
    // 右向きと上向きが衝突する最短時間
	int Answer = (1 << 24);
	for (int i = 0; i <= 500000; i++) V1[i].clear();
	for (int i = 1; i <= N; i++) {
		if (!(D[i] == 'R' || D[i] == 'U')) continue;
		V1[X[i] + Y[i]].push_back(make_pair(X[i], D[i]));
	}
	for (int i = 0; i <= 500000; i++) {
		sort(V1[i].begin(), V1[i].end());
		for (int j = 0; j < (int)V1[i].size() - 1; j++) {
			if (!(V1[i][j].second == 'R' && V1[i][j + 1].second == 'U')) continue;
			Answer = min(Answer, V1[i][j + 1].first - V1[i][j].first);
		}
	}
	return Answer * 10;
}

int solve_02() {
    // 右向きと左向きが衝突する最短時間
	int Answer = (1 << 24);
	for (int i = 0; i <= 500000; i++) V2[i].clear();
	for (int i = 1; i <= N; i++) {
		if (!(D[i] == 'L' || D[i] == 'R')) continue;
		V2[Y[i]].push_back(make_pair(X[i], D[i]));
	}
	for (int i = 0; i <= 500000; i++) {
		sort(V2[i].begin(), V2[i].end());
		for (int j = 0; j < (int)V2[i].size() - 1; j++) {
			if (!(V2[i][j].second == 'R' && V2[i][j + 1].second == 'L')) continue;
			Answer = min(Answer, V2[i][j + 1].first - V2[i][j].first);
		}
	}
	return Answer * 5;
}

int main() {
    // 入力
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> X[i] >> Y[i] >> D[i];

	int FinalAns = (1 << 24);
	for (int t = 1; t <= 4; t++) {
		int val1 = solve_01(); FinalAns = min(FinalAns, val1);
		int val2 = solve_02(); FinalAns = min(FinalAns, val2);
		Rotate();   // 時計回りに90度回転
	}
	if (FinalAns == (1 << 24)) cout << "SAFE" << endl;
	else cout << FinalAns << endl;
	return 0;
}
