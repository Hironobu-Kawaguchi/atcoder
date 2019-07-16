// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// O - 1.14.STLの関数 (Standard Template Library)
// https://atcoder.jp/contests/apg4b/tasks/APG4b_o

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int a = 10, b = 5;

	int answer1 = min(a, b); // min関数
	cout << answer1 << endl;
	int answer2 = max(a, b); // max関数
	cout << answer2 << endl;

	swap(a, b);	// swap関数 2つの引数の値を交換
	cout << a << endl;
	cout << b << endl;

	vector<int> vec = { 2, 5, 2, 1 };

	reverse(vec.begin(), vec.end());	// reverse関数 配列の要素の並びを逆に
	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << endl;
	}

	sort(vec.begin(), vec.end());	// sort関数 配列の要素を小さい順に並び替え
	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << endl;
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
