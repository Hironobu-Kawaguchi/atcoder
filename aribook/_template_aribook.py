# 蟻本をPythonで (初級編)
# https://qiita.com/saba/items/affc94740aff117d2ca9

# 2-1 すべての基本 "全探索"

# スタック
from collections import deque
s = deque([])
s.append(1)  # [1]
s.append(2)  # [1, 2]
s.append(3)  # [1, 2, 3]
s.pop()      # 一番上から取り除く [1, 2, 3] -> [1, 2]
s.pop()      # [1, 2] -> [1]
s.pop()      # [1] -> []

# キュー    # スタックと同様に collections.deque で扱うことができます。スタックでは取り除くときに pop だったのが、キューだと popleft になっているだけです。
from collections import deque
q = deque([])
q.append(1)  # [1]
q.append(2)  # [1, 2]
q.append(3)  # [1, 2, 3]
q.popleft()  # 一番下から取り除く [1, 2, 3] -> [2, 3]
q.popleft()  # [2, 3] -> [3]
q.popleft()  # [3] -> []

