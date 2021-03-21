// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// N - 1.13.配列
// https://atcoder.jp/contests/apg4b/tasks/APG4b_n

#include <iostream>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

int main() {
	vector<int> vec = { 1, 2, 3 };
	vec.push_back(10); // 末尾に10を追加
	// vecの全要素を出力
	for (int i = 0; i < vec.size(); i++) {
		cout << vec.at(i) << endl;
	}

	vec = vector<int>(100, 2); // 100要素の配列 {2, 2, ... , 2, 2} で上書き
	cout << vec.size() << endl;

	int N;
	cin >> N;
	vector<int> math(N); // N個の数学の点数データ
	vector<int> english(N); // N個の英語の点数データ
	// 数学の点数データを受け取る
	for (int i = 0; i < N; i++) {
		cin >> math.at(i);
	}
	// 英語の点数データを受け取る
	for (int i = 0; i < N; i++) {
		cin >> english.at(i);
	}
	// 合計点を出力
	for (int i = 0; i < N; i++) {
		cout << math.at(i) + english.at(i) << endl;
	}
}

/*
int main() {
	// 文字列
	string str; // 文字列変数を宣言
	str = "abcd"; // 'a', 'b', 'c', 'd' という文字(char)の列を代入
	cout << str.at(0) << endl; // 1つ目である'a'を出力
	cout << str.size() << endl; // 文字列の長さである4を出力

	// 配列
	vector<int> vec; // int型の配列変数vecを宣言
	vec = { 25, 100, 64 }; // 25, 100, 64 という整数(int)の列を代入
	cout << vec.at(0) << endl; // 1つめである25を出力
	cout << vec.size() << endl; // 配列の長さである3を出力

	// 3個の入力を受け取れるように 3要素の配列 {0, 0, 0} で初期化
	vector<int> vec2(3);
	// atを使って1つずつ入力
	cin >> vec2.at(0) >> vec2.at(1) >> vec2.at(2);
	// 和を出力
	cout << vec2.at(0) + vec2.at(1) + vec2.at(2) << endl;

	// 10要素の配列で初期化
	vector<int> vec3(10);
	// 10個の入力をfor文で受け取る
	for (int i = 0; i < 10; i++) {
		cin >> vec3.at(i);
	}
	cout << vec3.size() << endl;
}
*/

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント: 
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します 
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
