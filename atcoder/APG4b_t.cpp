// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// T - 2.03.多次元配列
// https://atcoder.jp/contests/apg4b/tasks/APG4b_t

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {

	// int型の2次元配列(3×4要素の)の宣言
	vector<vector<int>> data(3, vector<int>(4));

	// 入力 (2重ループを用いる)
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> data.at(i).at(j);
		}
	}

	data.size();  // 3 (縦の要素数) (12ではないことに注意!)
	data.at(0).size();  // 4 (横の要素数)

	// 0の個数を数える
	int count = 0;

	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 4; j++) {

			// 上からi番目、左からj番目の画素が0かを判定
			if (data.at(i).at(j) == 0) {
				count++;
			}

		}
	}

	cout << count << endl;

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
