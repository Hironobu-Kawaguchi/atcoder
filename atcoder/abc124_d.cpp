// D - Handstand
// https://atcoder.jp/contests/abc124/tasks/abc124_d

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;
	string S;
	cin >> S;

	vector<int> Nums;
	int now = 1; //今見ている数
	int cnt = 0; //nowがいくつ並んでいるか
	for (int i = 0; i < N; i++)
	{
		if (S[i] == (char)('0' + now)) cnt++;
		else {
			Nums.push_back(cnt);
			now = 1 - now; //0と1を切り替える時の計算 now ^= 1;
			cnt = 1; //新しいのをカウントし始める
		}
	}
	if (cnt != 0) Nums.push_back(cnt);

	//1-0-1-0-1-0-1って感じの配列が欲しい
	//1-0-1-0みたいに0で終わってたら、適当に１つ足す
	if (Nums.size() % 2 == 0) Nums.push_back(0);

	int Add = 2 * K + 1;

	//累積和を作る
	// 0 1 2 3 4 5 6
	//  0 1 2 3 4 5

	vector<int> sum(Nums.size() + 1);
	for (int i = 0; i < Nums.size(); i++)
	{
		sum[i + 1] = sum[i] + Nums[i];
	}


	int ans = 0;
	//1-0-1...の1から始めるので、偶数番目だけ見る
	for (int i = 0; i < Nums.size(); i += 2)
	{
		//次のleft, rightを計算する [left, right)
		int left = i;
		int right = min(i + Add, (int)Nums.size());
		int tmp = sum[right] - sum[left];

		ans = max(tmp, ans);
	}

	cout << ans << endl;
}



// #include<iostream>
// #include<vector>
// #include<algorithm>
// #include<string>
// using namespace std;

// int main() {
// 	int N, K;
// 	cin >> N >> K;
// 	string S;
// 	cin >> S;

// 	vector<int> Nums;
// 	int now = 1; //今見ている数
// 	int cnt = 0; //nowがいくつ並んでいるか
// 	for (int i = 0; i < N; i++)
// 	{
// 		if (S[i] == (char)('0' + now)) cnt++;
// 		else {
// 			Nums.push_back(cnt);
// 			now = 1 - now; //0と1を切り替える時の計算 now ^= 1;
// 			cnt = 1; //新しいのをカウントし始める
// 		}
// 	}
// 	if (cnt != 0) Nums.push_back(cnt);

// 	//1-0-1-0-1-0-1って感じの配列が欲しい
// 	//1-0-1-0みたいに0で終わってたら、適当に１つ足す
// 	if (Nums.size() % 2 == 0) Nums.push_back(0);

// 	int Add = 2 * K + 1;

// 	int ans = 0;

// 	int left = 0;  
// 	int right = 0; 
// 	int tmp = 0;// [left, right) のsum

// 	//1-0-1...の1から始めるので、偶数番目だけ見る
// 	for (int i = 0; i < Nums.size(); i += 2)
// 	{
// 		int Nextleft = i;
// 		int Nextright = min(i + Add, (int)Nums.size());

// 		//左端を移動する
// 		while (Nextleft > left) {
// 			tmp -= Nums[left];
// 			left++;
// 		}
// 		//右端を移動する
// 		while (Nextright > right) {
// 			tmp += Nums[right];
// 			right++;
// 		}

// 		ans = max(tmp, ans);
// 	}

// 	cout << ans << endl;
// }



// #include<iostream>
// #include<vector>
// #include<algorithm>
// #include<string>
// using namespace std;

// int main() {
// 	int N, K;
// 	cin >> N >> K;
// 	string S;
// 	cin >> S;

// 	vector<int> Nums;
// 	int now = 1; //今見ている数
// 	int cnt = 0; //nowがいくつ並んでいるか
// 	for (int i = 0; i < N; i++)
// 	{
// 		if (S[i] == (char)('0' + now)) cnt++;
// 		else {
// 			Nums.push_back(cnt);
// 			now = 1 - now; //0と1を切り替える時の計算 now ^= 1;
// 			cnt = 1; //新しいのをカウントし始める
// 		}
// 	}
// 	if (cnt != 0) Nums.push_back(cnt);

// 	//1-0-1-0-1-0-1って感じの配列が欲しい
// 	//1-0-1-0みたいに0で終わってたら、適当に１つ足す
// 	if (Nums.size() % 2 == 0) Nums.push_back(0);

// 	int Add = 2 * K + 1;

// 	int ans = 0;

// 	//1-0-1...の1から始めるので、偶数番目だけ見る
// 	for (int i = 0; i < Nums.size(); i += 2)
// 	{
// 		int tmp = 0;

// 		int left = i;
// 		int right = min(i + Add, (int)Nums.size());
// 		for (int j = left; j < right; j++)
// 		{
// 			tmp += Nums[j];
// 		}
// 		ans = max(tmp, ans);
// 	}

// 	cout << ans << endl;
// }



// #include <iostream>
// #include <algorithm>
// #include <string>
// #include <vector>
// #include <tuple>
// #include <queue>
// // #include <bits/stdc++.h>
// using namespace std;

// int main() {
// 	int N, K;
// 	string S;
// 	cin >> N >> K;
// 	cin >> S;

// 	vector<int> Nums;
// 	char now = '1';	// 今見ている数
// 	int cnt = 0;	// nowがいくつ並んでいるか

// 	for (int i = 0; i < N; i++) {
// 		if (S.at(i) == now) {
// 			cnt++;
// 		}
// 		else {
// 			Nums.push_back(cnt);
// 			now = S.at(i);
// 			cnt = 1;
// 		}
// 	}
// 	if (cnt != 0) Nums.push_back(cnt);
// 	if (Nums.size() % 2 == 0) Nums.push_back(0);

// 	// 累積和
// 	vector<int> sum(Nums.size() + 1, 0);
// 	for (int i = 0; i < Nums.size(); i++) {
// 		sum.at(i + 1) = sum.at(i) + Nums.at(i);
// 	}

// 	int Add = 2 * K + 1;
// 	int ans = 0;
// 	for (int i = 0; i < Nums.size(); i += 2) {
// 		int right;
// 		right = min(i + Add, (int)Nums.size());
// 		int tmp = sum.at(right) - sum.at(i);
// 		ans = max(tmp, ans);
// 	}

// 	cout << ans << endl;
// 	return 0;
// }
