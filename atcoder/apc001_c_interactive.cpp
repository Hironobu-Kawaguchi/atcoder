// https://atcoder.jp/contests/apc001/tasks/apc001_c
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

map<int, int> mp;
int n;
int ask(int i) {
    i %= n;
    if (mp.count(i)) return mp[i];
    cout << i << endl;
    string s;
    cin >> s;
    if (s[0] == 'V') exit(0);
    return mp[i] = (s[0]  == 'M');
}

int g(int i, int j) { return (j-i+n)%n;}

int main() {
	cin >> n;
    int l = 0, r = n/2;
    int a = ask(l);
    int b = ask(r);
    if ((a^b) == g(l,r)%2) {
        swap(l,r); r += n;
    }
    while (1) {
        int c = (l+r)>>1;
        if ((ask(l)^ask(c)) == g(l,c)%2)   l = c;
        else                               r = c;
    }
	return 0;
}
