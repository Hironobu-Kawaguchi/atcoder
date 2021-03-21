// https://atcoder.jp/contests/past201912-open/tasks/past201912_f
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
	string s;
	cin >> s;
    vector<string> v;
    int start = 0, end;
    for (int i = 1; i < s.size(); i++) {
        if(s[i]>='A' && s[i]<='Z') {
            end = i;
            s[start] -= 'A' - 'a';
            s[end]   -= 'A' - 'a';
            v.push_back(s.substr(start, end-start+1));
            start = i+1;
            i++;
        }
    }
    sort(v.begin(), v.end());
    for (string x : v) {
        x[0] += 'A' - 'a';
        x[x.size()-1] += 'A' - 'a';
        cout << x;
    }
	cout << endl;
	return 0;
}
