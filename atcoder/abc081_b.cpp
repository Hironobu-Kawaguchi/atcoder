// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// B - Shift only
// https://atcoder.jp/contests/abc081/tasks/abc081_b

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
typedef long long ll;
const ll LINF = 1001002003004005006ll;


int main() {
	int n;
	cin >> n;
	ll a;
	ll ans = LINF;
	rep(i,n) {
		cin >> a;
		ll cnt = 0;
		while ((a&1)==0) {
			++cnt;
			a >>= 1;
		}
		if (cnt < ans) ans = cnt;
	}
	cout << ans << endl;
	return 0;
}


// int main() {
// 	int N;
// 	cin >> N;
// 	int ans = 30;	// 2**30 = 1073741824 (>10**9)
// 	for (int i = 0; i < N; i++) {
// 		int A;
// 		cin >> A;
// 		int cnt = 0;
// 		while (A > 0) {	// 各Aについて、2で何回割り切れるかカウント(cnt)
// 			if (A % 2 == 0)	{
// 				A /= 2;
// 				cnt++;
// 			}
// 			else {
// 				break;
// 			}
// 		}
// 		if (ans > cnt) {	// 各Aのcntの最小値をansに格納
// 			ans = cnt;
// 		}
// 	}
// 	cout << ans << endl;
// }

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
