#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_s(i, s, n) for (int i = (int)(s); i < (int)(n); i++)
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;

#define MOD 1000000007

int main()
{
  int N, M, D, K;
  cin >> N >> M >> D >> K;

  vector<vector<tuple<int, int, int>>> G(N);
  vector<tuple<int, int, int>> to;
  rep(i, M)
  {
    int u, v, w;
    cin >> u >> v >> w;
    u--;
    v--;
    G[u].push_back(make_tuple(v, w, i));
    G[v].push_back(make_tuple(u, w, i));
    to.push_back(make_tuple(u, v, w));
  }

  vector<set<tuple<int, int>>> uc_list(D);
  vector<int> r;
  rep(i, K * D)
  {
    r.push_back(i % D + 1);
    if (i < M)
    {
      uc_list[i % D].insert(to[i]);
    }
  }

  int bfs(int start, set<tuple<int, int>> under_construction)
  {
    vector<bool> visited(N, false);
    vector<int> dist(N, 1001001001001);
    priority_queue<tuple<int, int>, vector<tuple<int, int>>, greater<tuple<int, int>>> hq;
    hq.push(make_tuple(0, start));
    while (!hq.empty())
    {
      int d, now;
      tie(d, now) = hq.top();
      hq.pop();
      if (visited[now])
        continue;
      dist[now] = d;
      visited[now] = true;
      for (auto tpl : G[now])
      {
        int nxt, w, idx;
        tie(nxt, w, idx) = tpl;
        if (visited[nxt])
          continue;
        if (under_construction.count(make_tuple(now, nxt)))
          continue;
        if (under_construction.count(make_tuple(nxt, now)))
          continue;
        hq.push(make_tuple(d + w, nxt));
      }
    }
    int ret = 0;
    rep(i, N)
    {
      ret += dist[i];
    }
    return ret;
  }

  int score_change(vector<int> swap_idx)
  {
    vector<set<tuple<int, int>>> swap_set;
    vector<int> swap_day;
    rep(i, 2)
    {
      swap_day.push_back(r[swap_idx[i]]);
      if (swap_idx[i] < M)
      {
        swap_set.push_back(set<tuple<int, int>>{to[swap_idx[i]]});
      }
      else
      {
        swap_set.push_back(set<tuple<int, int>>());
      }
    }
    int ret = 0;
    vector<int> node_list;
    rep(i, 2)
    {
      if (swap_set[i].size() == 0)
        continue;
      for (auto tpl : swap_set[i])
      {
        rep(j, 2)
        {
          node_list.push_back(get<j>(tpl));
        }
      }
    }
    sort(node_list.begin(), node_list.end());
    node_list.erase(unique(node_list.begin(), node_list.end()), node_list.end());
    rep(i, node_list.size())
    {
      rep(j, 2)
      {
        ret += bfs(node_list[i], uc_list[swap_day[j] - 1] - swap_set[j] | swap_set[1 - j]);
        ret -= bfs(node_list[i], uc_list[swap_day[j] - 1]);
      }
    }
    return ret;
  }

  void swap_link(vector<int> swap_idx)
  {
    set<tuple<int, int>> st0, st1;
    if (swap_idx[0] < M)
    {
      st0 = set<tuple<int, int>>{to[swap_idx[0]]};
    }
    if (swap_idx[1] < M)
    {
      st1 = set<tuple<int, int>>{to[swap_idx[1]]};
    }
    uc_list[r[swap_idx[0]] - 1] -= st0;
    uc_list[r[swap_idx[0]] - 1] |= st1;
    uc_list[r[swap_idx[1]] - 1] -= st1;
    uc_list[r[swap_idx[1]] - 1] |= st0;
    r[swap_idx[0]], r[swap_idx[1]] = r[swap_idx[1]], r[swap_idx[0]];
    return;
  }

  int cnt = 0;
  while (clock() < 5.8 * CLOCKS_PER_SEC)
  {
    vector<int> swap_idx = {rand() % (K * D), rand() % (K * D)};
    if (swap_idx[0] >= M && swap_idx[1] >= M)
      continue;
    if (r[swap_idx[0]] == r[swap_idx[1]])
      continue;
    int sc = score_change(swap_idx);
    int NUM_LOOPS = 500;
    double T;
    if (cnt < NUM_LOOPS)
    {
      T = 500000 - 450000 * (cnt / NUM_LOOPS);
    }
    else
    {
      T = 1.0;
    }
    double probability = exp(min((-sc) / T, 0));
    cnt++;
    if (rand() / (RAND_MAX + 1.0) < probability)
    {
      swap_link(swap_idx);
    }
  }

  rep(i, M)
  {
    cout << r[i] << endl;
  }
}