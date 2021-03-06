// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX17 - 果物屋さんでお買い物 / 2.02
// https://atcoder.jp/contests/apg4b/tasks/APG4b_cf

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N, S;
	cin >> N >> S;
	vector<int> A(N), P(N);
	for (int i = 0; i < N; i++) {
		cin >> A.at(i);
	}
	for (int i = 0; i < N; i++) {
		cin >> P.at(i);
	}

	// リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
	// ここにプログラムを追記
	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (A.at(i) + P.at(j) == S) {
				ans++;
			}
		}

	}
	cout << ans << endl;
}

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
