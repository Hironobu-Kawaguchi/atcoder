#include <bits/stdc++.h>
using namespace std;
#define MAXN 1000005
#define INF 1001001001001

struct Edge{
    int to, cost, idx;
};
vector<Edge> G[MAXN];

int N, M, D, K;
int to[MAXN][3];

set<pair<int, int>> uc_list[MAXN];
int r[MAXN];

bool visited[MAXN];
int dist[MAXN];

int bfs(int start, set<pair<int, int>> under_construction){
    memset(visited, false, sizeof visited);
    memset(dist, 0x3f, sizeof dist);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> hq;
    hq.push({0, start});
    while(!hq.empty()){
        int d = hq.top().first, now = hq.top().second;
        hq.pop();
        if(visited[now]) continue;
        dist[now] = d;
        visited[now] = true;
        for(int i = 0; i < G[now].size(); i++){
            int nxt = G[now][i].to, w = G[now][i].cost, idx = G[now][i].idx;
            if(visited[nxt]) continue;
            if(under_construction.count({now, nxt})) continue;
            hq.push({d + w, nxt});
        }
    }
    int ret = 0;
    for(int i = 0; i < N; i++){
        ret += dist[i];
    }
    return ret;
}

int score_change(int a, int b){
    set<pair<int, int>> swap_set[2];
    int swap_day[2];
    for(int i = 0; i < 2; i++){
        swap_day[i] = r[a + i];
        if(a + i < M){
            swap_set[i].insert({to[a + i][0], to[a + i][1]});
        }
    }
    int ret = 0;
    vector<int> node_list;
    for(int i = 0; i < 2; i++){
        if(swap_set[i].empty()) continue;
        for(pair<int, int> tpl : swap_set[i]){
            for(int j = 0; j < 2; j++){
                node_list.push_back(tpl.first);
                node_list.push_back(tpl.second);
            }
        }
    }
    sort(node_list.begin(), node_list.end());
    node_list.erase(unique(node_list.begin(), node_list.end()), node_list.end());
    for(int i : node_list){
        for(int j = 0; j < 2; j++){
            ret += bfs(i, uc_list[swap_day[j] - 1] - swap_set
        }
    }
}