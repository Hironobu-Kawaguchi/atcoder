// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// EX8 - たこ焼きセット / 1.08
// https://atcoder.jp/contests/apg4b/tasks/APG4b_co

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int p;
	cin >> p;

	// パターン1
	//if (p == 1) {
	//	int price;
	//	cin >> price;
	//}

	// パターン2
	if (p == 2) {
		string text;
		cin >> text;
		cout << text << "!" << endl;
		//int price;
		//cin >> text >> price;
	}

	int price;
	cin >> price;
	int N;
	cin >> N;

	//cout << text << "!" << endl;
	cout << price * N << endl;
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
