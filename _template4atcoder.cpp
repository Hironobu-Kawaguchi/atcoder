#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<tuple>
#include<queue>
using namespace std;

int W, H; // 横幅と縦幅
int MAX_W = 500, MAX_H = 500;
vector<vector<char>> maze(MAX_H, vector<char>(MAX_W));
vector<vector<bool>> reached(MAX_H, vector<bool>(MAX_W));
int sx, sy, gx, gy;

void dfs(int x, int y) {
	// 迷路の外側か壁の場合は何もしない
	if (x < 0 || W <= x || y < 0 || H <= y || maze.at(y).at(x) == '#') return;
	// 以前に到達していたら何もしない
	if (reached.at(y).at(x)) return;
	reached.at(y).at(x) = true; // 到達したよ
	// 4 方向を試す
	dfs(x + 1, y); // 右
	dfs(x - 1, y); // 左
	dfs(x, y + 1); // 下
	dfs(x, y - 1); // 上
}

int main() {
	int N;
	cin >> N;

	dfs(sx, sy);

    string ans;

	cout << ans << endl;
	return 0;
}
