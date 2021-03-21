// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX18 - ゲーム大会 / 2.03
// https://atcoder.jp/contests/apg4b/tasks/APG4b_ce

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int N, M;
	cin >> N >> M;
	vector<int> A(M), B(M);
	for (int i = 0; i < M; i++) {
		cin >> A.at(i) >> B.at(i);
	}

	// ここにプログラムを追記
	// (ここで"試合結果の表"の2次元配列を宣言)
	vector<vector<char>> R(N, vector<char>(N, '-'));
	for (int i = 0; i < M; i++){
		R.at(A.at(i) - 1).at(B.at(i) - 1) = 'o';
		R.at(B.at(i) - 1).at(A.at(i) - 1) = 'x';
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << R.at(i).at(j);
			if (j < N-1) {
				cout << ' ';
			}
		}
		cout << endl;
	}
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
