// https://codeforces.com/contest/1466/problem/C
// 回文には必ず2文字か3文字の回文が含まれるので、貪欲に変えていく
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

const int N = 100'007;

int n;
char in[N];
bool used[N];

void solve(){
	scanf("%s", in + 1);
	n = strlen(in + 1);
	
	for(int i = 1; i <= n; ++i)
		used[i] = false;
	
	int ans = 0;
	for(int i = 2; i <= n; ++i){
		bool use_need = false;
		if(in[i] == in[i - 1] && !used[i - 1])
			use_need = true;

		if(i > 2 && in[i] == in[i - 2] && !used[i - 2])
			use_need = true;

		used[i] = use_need;
		ans += used[i];
	}
	
	printf("%d\n", ans);
}

int main(){
	int cases;
	scanf("%d", &cases);
	
	while(cases--)
		solve();
	return 0;
}

// dame
// const int MAX_L = 200005;
// int n, k;
// string S;
// int sa[MAX_L + 1], lcp[MAX_L], rankx[MAX_L + 1], tmp[MAX_L + 1];

// bool compare_sa(int i, int j) {
//     if (rankx[i] != rankx[j]) return rankx[i] < rankx[j];
//     else {
//         int ri = i + k <= n ? rankx[i+k] : -1;
//         int rj = j + k <= n ? rankx[j+k] : -1;
//         return ri < rj;
//     }
// }

// void construct_sa(string S, int *sa) {
//     n = S.length();
//     rep(i,MAX_L+1) sa[i]=0, rankx[i]=0, tmp[i]=0;
//     for (int i = 0; i < n; i++) {
//         sa[i] = i;
//         rankx[i] = i < n ? S[i] : -1;
//     }
//     for (int k = 1; k <= n; k*=2) {
//         sort(sa, sa + n + 1, compare_sa);
//         tmp[sa[0]] = 0;
//         for (int i = 1; i <= n; i++) {
//             tmp[sa[i]] = tmp[sa[i-1]] + (compare_sa(sa[i-1], sa[i]) ? 1 : 0);
//         }
//         for (int i = 0; i <= n; i++) {
//             rankx[i] = tmp[i];
//         }
//     }
// }

// void construct_lcp(string S, int *sa, int *lcp) {
//     rep(i,MAX_L) lcp[i]=0;
//     int n = S.length();
//     for (int i = 0; i <= n; i++) rankx[sa[i]] = i;
//     int h = 0;
//     lcp[0] = 0;
//     for (int i = 0; i < n; i++) {
//         int j = sa[rankx[i] - 1];
//         if (h > 0) h--;
//         for (; j + h < n && i + h < n; h++) {
//             if (S[j+h] != S[i+h]) break;
//         }
//         lcp[rankx[i] - 1] = h;
//     }
// }

// int solve() {
//     cin >> S;
//     int n = S.length();
//     string T = S;
//     reverse(T.begin(), T.end());
//     S += '$' + T;

//     construct_sa(S, sa);
//     construct_lcp(S, sa, lcp);
//     for (int i = 0; i <= S.length(); i++) rankx[sa[i]] = i;
//     // construct_rmq(lcp, S.length() - 1);
//     rep(i,S.length()) cout << lcp[i] << ' ';
//     cout << endl;

//     // ll ans = 0;
// 	// cout << ans << "\n";
// 	return 0;
// }

// int main() {
// 	int t;
// 	cin >> t;
//     rep(i,t) solve();
//     return 0;

// }
