// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// H - 1.07.条件式の結果とbool型
// https://atcoder.jp/contests/APG4b/tasks/APG4b_h

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	cout << (5 < 10) << endl; // 真
	cout << (5 > 10) << endl; // 偽

	// 1は真を表すのでhelloと出力される
	if (1) {
		cout << "hello" << endl;
	}
	// 0は偽を表すのでこのifの中は実行されない
	if (0) {
		cout << "world" << endl;
	}

	// 1と書くよりも真だということがわかりやすい
	if (true) {
		cout << "hello" << endl;
	}
	// 0と書くよりも偽だということがわかりやすい
	if (false) {
		cout << "world" << endl;
	}

	int x;
	cin >> x;
	bool a = true;
	bool b = x < 10; // xが10未満のときtrue そうでないときfalseになる
	bool c = false;
	if (a && b) {
		cout << "hello" << endl;
	}
	if (c) {
		cout << "world" << endl;
	}

	bool aa = 10; // 10はtrue
	bool bb = 0; // 0はfalse
	cout << aa << endl;
	cout << bb << endl;
	// 100はtrue
	if (100) {
		cout << "hello" << endl;
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
