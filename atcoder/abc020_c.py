# https://atcoder.jp/contests/abc020/tasks/abc020_c

from collections import deque

def is_ok(x: int) -> bool:
    D = [[T+1] * W for _ in range(H)]
    D[sr][sc] = 0
    drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((sr, sc))
    while q:
        r, c = q.popleft()
        curr = D[r][c]
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if (0 <= nr < H) and (0 <= nc < W):
                next_ = curr + (x if s[nr][nc] == '#' else 1)
                if next_ < D[nr][nc]:
                    D[nr][nc] = next_
                    q.append((nr, nc))
    return D[gr][gc] <= T

def binary_search(ng: int, ok: int) -> int:
    while abs(ng - ok) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

H, W, T = map(int, input().split())
s = [input() for _ in range(H)]

for r, row in enumerate(s):
    for c, cell in enumerate(row):
        if cell == 'S':
            sr, sc = r, c
        elif cell == 'G':
            gr, gc = r, c
ans = binary_search(ng=T+1, ok=1)
print(ans)
