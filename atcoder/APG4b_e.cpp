// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// E - 1.04.変数と型
// https://atcoder.jp/contests/APG4b/tasks/APG4b_e

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {

	int name;
	name = 10;
	cout << name << endl;     // 10
	cout << name + 2 << endl; // 10 + 2 → 12
	cout << name * 3 << endl; // 10 * 3 → 30
	cout << endl;

	int a = 10;
	int b;
	b = a; // aの値がコピーされ、bに10が代入される
	a = 5; // aの値は5に書き換わるが、bは10のまま
	cout << a << endl;
	cout << b << endl;
	cout << endl;

	int aa = 10, bb = 5;
	cout << aa << endl;
	cout << bb << endl;
	cout << endl;

	int i = 30;
	double d = 1.5;
	string s = "Hello";
	cout << i << endl;
	cout << d << endl;
	cout << s << endl;
	cout << i + d << endl;
	cout << i * d << endl;
	cout << 45 / 2 << endl; //小数点以下切り捨て
	cout << i * d / 2 << endl; //小数点以下も残る
	/*	以下の処理はコンパイルエラー
	cout << s + i << endl; // string型とint型
	cout << s * i << endl; // string型とint型
	cout << s + d << endl; // string型とdouble型
	*/
	cout << endl;

	int ii = 10;
	double dd = ii; // doubleとintは互いに代入できる（小数点以下切り捨て）
	/*	以下の処理はコンパイルエラー
	string s = "Hello";
	i = s; // int型とstring型は互いに代入できない
	*/
	cout << dd << endl;
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
