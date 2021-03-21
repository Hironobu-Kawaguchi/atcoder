// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// M - 1.12.文字列と文字
// https://atcoder.jp/contests/apg4b/tasks/APG4b_m

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	string str1, str2;
	cin >> str1;
	str2 = ", world!";	// string型は""で囲う

	string str = str1 + str2;	// +でstring型の結合ができる
	cout << str << endl;
	cout << str.size() << endl;
	cout << str.at(0) << endl;
	cout << str.at(4) << endl;

	char c = 'a';	// char型は''で囲う
	cout << c << endl;
	char cc = str.at(0); // char型の値が得られる
	cout << cc << endl;
	cout << str + cc << endl;	// +でstring型とchar型の結合ができる

	str.at(0) = 'M'; // char型の'M'
	cout << str << endl;

	int count = 0;
	for (int i = 0; i < str.size(); i++) {
		if (str.at(i) == 'l') {	// 'l'の数をカウント
			count++;
		}
	}
	cout << count << endl;

	char a, b;
	cin >> a >> b;	// char型の変数にcinで入力すると一文字ずつ取り出すことができる
	cout << a << endl;
	cout << b << endl;
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
