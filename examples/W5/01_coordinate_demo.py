"""
W5 範例 1：座標系統示範
學習重點：理解 2D 座標表示
"""

# 座標表示 (x, y)
origin = (0, 0)        # 原點
front = (0, 1)         # 前方
right = (1, 0)         # 右方
diagonal = (1, 1)      # 對角

print("===== 座標系統示範 =====")
print(f"原點：{origin}")
print(f"前方 1 單位：{front}")
print(f"右方 1 單位：{right}")
print(f"對角位置：{diagonal}")

# 路徑列表
path = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

print("\n===== 正方形路徑 =====")
for i, pos in enumerate(path):
    print(f"第 {i+1} 點：{pos}")

# 計算距離
import math

def distance(p1, p2):
    """計算兩點間距離"""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return math.sqrt(dx**2 + dy**2)

print("\n===== 距離計算 =====")
d = distance((0, 0), (3, 4))
print(f"從 (0,0) 到 (3,4) 的距離：{d}")
