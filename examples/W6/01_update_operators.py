"""
W6 範例 1：變數更新運算
學習重點：+=, -=, *=, /= 的使用
"""

print("===== 變數更新運算 =====\n")

# += 加法更新
height = 10
print(f"初始高度：{height}")
height += 5
print(f"上升 5 後：{height}")
height += 3
print(f"再上升 3 後：{height}\n")

# -= 減法更新
battery = 100
print(f"初始電量：{battery}%")
battery -= 20
print(f"消耗 20% 後：{battery}%")
battery -= 15
print(f"再消耗 15% 後：{battery}%\n")

# *= 乘法更新
speed = 5
print(f"初始速度：{speed}")
speed *= 2
print(f"加速 2 倍後：{speed}")
speed *= 1.5
print(f"再加速 1.5 倍後：{speed}\n")

# /= 除法更新
distance = 100
print(f"初始距離：{distance}")
distance /= 2
print(f"減半後：{distance}")
distance /= 2
print(f"再減半後：{distance}")
