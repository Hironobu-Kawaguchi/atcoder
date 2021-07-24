// http://codeforces.com/contest/1553/problem/D
// https://codeforces.com/blog/entry/93105
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__);fflush(stderr);
#else
	#define eprintf(...) 42
#endif

using ll = long long;
using ld = long double;
using uint = unsigned int;
using ull = unsigned long long;
template<typename T>
using pair2 = pair<T, T>;
using pii = pair<int, int>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
	return (ull)rng() % B;
}

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second

clock_t startTime;
double getCurrentTime() {
	return (double)(clock() - startTime) / CLOCKS_PER_SEC;
}

const int N = 200200;
int n, m;
char s[N], t[N];

bool solve() {
	scanf("%s %s", s, t);
	n = strlen(s);
	m = strlen(t);
	if (n < m) return false;
	int p = (n - m) & 1;
	int q = 0;
	int k = 0;
	for (int i = p; i < n; i++) {
		if (k == 1) {
			k = 0;
			continue;
		}
		if (q < m && s[i] == t[q]) {
			q++;
		} else {
			k++;
		}
	}
	return q == m;
}

int main()
{
	startTime = clock();
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	while(T--) {
		if (solve())
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}