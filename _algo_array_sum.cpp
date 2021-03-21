// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// V - 2.05.再帰関数 (再帰関数の実装例)
// 配列の要素の総和： array_sum
// https://atcoder.jp/contests/apg4b/tasks/APG4b_v

#include <iostream>
#include <algorithm>
#include <vector>
// #include <bits/stdc++.h>
using namespace std;

// (補助関数)
// dataのi番目以降の要素の総和を計算する
int array_sum_from_i(vector<int>& data, int i) {
	// ベースケース
	if (i == data.size()) {
		return 0;  // 対象の要素がないので総和は0
	}
	// 再帰ステップ
	int s = array_sum_from_i(data, i + 1);  // i+1番目以降の要素の総和
	return data.at(i) + s;  // 「i番目以降の要素の総和」=「i番目の要素」+ s
}

// dataの全ての要素の総和を計算する
int array_sum(vector<int> & data) {
	return array_sum_from_i(data, 0);
}

int main() {
	vector<int> a = { 0, 3, 9, 1, 5 };
	cout << array_sum(a) << endl;   // 0 + 3 + 9 + 1 + 5 = 18
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
