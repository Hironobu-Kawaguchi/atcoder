// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// J - 1.09.複合代入演算子
// https://atcoder.jp/contests/APG4b/tasks/APG4b_j

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	int z = 5;
	z += 1 + 2;
	cout << z << endl;

	int a = 5;
	a -= 2;
	cout << a << endl;

	int b = 3;
	b *= 1 + 2;
	cout << b << endl;

	int c = 4;
	c /= 2;
	cout << c << endl;

	int d = 5;
	d %= 2;
	cout << d << endl;

	int x = 5;
	x++;
	cout << x << endl;

	int y = 5;
	y--;
	cout << y << endl;
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
