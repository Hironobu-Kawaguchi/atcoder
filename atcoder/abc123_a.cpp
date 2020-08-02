// A - Five Antennas
// https://atcoder.jp/contests/abc123/tasks/abc123_a

#include<iostream>
#include<string>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;


int main() {

	//入力
	int a, b, c, d, e;
	int k;
	cin >> a >> b >> c >> d >> e;
	cin >> k;

	//処理
	string ans;
	int L = e - a;
	if (L <= k) ans = "Yay!";
	else ans = ":(";

	//出力
	cout << ans << endl;
}



// #include<iostream>
// #include<string>
// #include<map>
// #include<algorithm>
// #include<vector>
// using namespace std;


// int main() {

// 	//入力
// 	int a, b, c, d, e;
// 	int k;
// 	cin >> a >> b >> c >> d >> e;
// 	cin >> k;

// 	//処理
// 	vector<int> v = { a, b, c, d, e };
// 	bool ok = true;
// 	//i, jの組み合わせを全部調べる
// 	for (int i = 0; i < v.size(); i++)
// 	{
// 		for (int j = 0; j < v.size(); j++)
// 		{
// 			//kを越えている値を見つけたら、okの値を更新する
// 			if (v[j] - v[i] > k) {
// 				ok = false;
// 			}
// 		}
// 	}
// 	string ans;
// 	if (ok) ans = "Yay!";
// 	else ans = ":(";

// 	//出力
// 	cout << ans << endl;
// }
