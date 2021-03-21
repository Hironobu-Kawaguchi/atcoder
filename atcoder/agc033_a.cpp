// AtCoder_Cpp.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//
// A - Darker and Darker
// https://atcoder.jp/contests/agc033/tasks/agc033_a

#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>
#include <queue>
// #include <bits/stdc++.h>
using namespace std;

int N, M;
int MAX = 1000;
vector<vector<int>>  D(MAX, vector<int>(MAX));
vector<vector<char>> S(MAX, vector<char>(MAX));
vector<int> dx = { 0, 1,  0, -1 };
vector<int> dy = { 1, 0, -1,  0 };
queue<pair<int, int>> Q;

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> S.at(i).at(j);
			if (S.at(i).at(j) == '#') {
				Q.push({ i,j });
			}
		}
	}

	int ans = 0;
	while (!Q.empty()) {
		int x, y;
		tie(x, y) = Q.front();
		Q.pop();
		int d = D.at(x).at(y);
		ans = d;
		for (int k = 0; k < 4; k++) {
			int px = x + dx.at(k);
			int py = y + dy.at(k);
			if (px < 0 || px >= N || py < 0 || py >= M) continue;
			if (S.at(px).at(py) == '.') {
				Q.push({ px,py });
				S.at(px).at(py) = '#';
				D.at(px).at(py) = d + 1;
			}
		}
	}

	cout << ans << endl;
	return 0;
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
