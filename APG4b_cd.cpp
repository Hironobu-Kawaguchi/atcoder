// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX19 - 九九の採点 / 2.04
// https://atcoder.jp/contests/apg4b/tasks/APG4b_cd

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// 参照渡しを用いて、呼び出し側の変数の値を変更する
void saiten(vector<vector<int>> &A, int &correct_count, int &wrong_count) {
	// 呼び出し側のAの各マスを正しい値に修正する
	// Aのうち、正しい値の書かれたマスの個数を correct_count に入れる
	// Aのうち、誤った値の書かれたマスの個数を wrong_count に入れる
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (A.at(i).at(j) == ((i + 1) * (j + 1))) {
				correct_count++;
			}
			else {
				wrong_count++;
				A.at(i).at(j) = (i + 1) * (j + 1);
			}
		}
	}
}


// -------------------
// ここから先は変更しない
// -------------------
int main() {
	// A君の回答を受け取る
	vector<vector<int>> A(9, vector<int>(9));
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> A.at(i).at(j);
		}
	}

	int correct_count = 0; // ここに正しい値のマスの個数を入れる
	int wrong_count = 0;   // ここに誤った値のマスの個数を入れる

	// A, correct_count, wrong_countを参照渡し
	saiten(A, correct_count, wrong_count);

	// 正しく修正した表を出力
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << A.at(i).at(j);
			if (j < 8) cout << " ";
			else cout << endl;
		}
	}
	// 正しいマスの個数を出力
	cout << correct_count << endl;
	// 誤っているマスの個数を出力
	cout << wrong_count << endl;
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
