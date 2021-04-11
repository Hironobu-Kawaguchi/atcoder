// https://atcoder.jp/contests/acl1/tasks/acl1_c
// https://atcoder.jp/contests/acl1/submissions/18927263
#include <bits/stdc++.h>
#include <atcoder/mincostflow>
using namespace std;
using namespace atcoder;
vector<int> dy = {1, 0};
vector<int> dx = {0, 1};
int main() {
    int N, M;
    cin >> N >> M;
    vector<string> S(N);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }
    int cnt = 0;  // 駒の数
    vector<int> yp, xp;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (S[i][j] == 'o') {
                cnt++;
                yp.push_back(i);
                xp.push_back(j);
            }
        }
    }
    int V = N * M + cnt + 2;   // s, 駒(cnt), 盤面(N*M), t
    mcf_graph<int, int> G(V);  // 最小費用流
    int MAX = N + M - 2;
    for (int i = 0; i < cnt; i++) {
        G.add_edge(0, i + 1, 1, 0);  // s-駒
    }
    for (int i = cnt + 1; i < cnt + 1 + N * M; i++) {
        G.add_edge(i, V - 1, 1, 0);  // 盤面-t
    }
    for (int i = 0; i < cnt; i++) {  // BFSで各駒の移動可能範囲に辺を追加する
        vector<vector<int>> d(N, vector<int>(M, -1));
        d[yp[i]][xp[i]] = 0;
        G.add_edge(i + 1, cnt + 1 + yp[i] * M + xp[i], 1, MAX);  // 駒-初期位置
        queue<pair<int, int>> Q;
        Q.push(make_pair(yp[i], xp[i]));
        while (!Q.empty()) {
            int y = Q.front().first;
            int x = Q.front().second;
            Q.pop();
            for (int j = 0; j < 2; j++) {
                int y2 = y + dy[j];
                int x2 = x + dx[j];
                if (y2 < N && x2 < M) {
                    if (d[y2][x2] == -1 && S[y2][x2] != '#') {
                        d[y2][x2] = d[y][x] + 1;
                        G.add_edge(i + 1, cnt + 1 + y2 * M + x2, 1, MAX - d[y2][x2]); // 駒-初期位置から移動できる盤面
                        Q.push(make_pair(y2, x2));
                    }
                }
            }
        }
    }
    cout << MAX * cnt - G.flow(0, V - 1).second << endl;
}