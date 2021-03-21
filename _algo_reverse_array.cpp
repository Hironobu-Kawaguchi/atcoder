// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// V - 2.05.再帰関数 (再帰関数の実装例)
// 配列の操作 reverse_array
// https://atcoder.jp/contests/apg4b/tasks/APG4b_v

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// dataのi番目以降の要素を逆順にした配列を返す
vector<int> reverse_array_from_i(vector<int>& data, int i) {
	// ベースケース
	if (i == data.size()) {
		vector<int> empty_array(0);  // 要素数0の配列
		return empty_array;
	}

	// 再帰ステップ
	vector<int> tmp = reverse_array_from_i(data, i + 1);  // dataのi+1番目以降の要素を逆順にした配列を得る
	tmp.push_back(data.at(i));  // 末尾にdataのi番目の要素を追加
	return tmp;
}

// 配列を逆順にしたものを返す
vector<int> reverse_array(vector<int> & data) {
	return reverse_array_from_i(data, 0);
}

int main() {
	vector<int> a = { 1, 2, 3, 4, 5 };
	vector<int> b = reverse_array(a);
	for (int i = 0; i < b.size(); i++) {
		cout << b.at(i) << endl;
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
