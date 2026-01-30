"""
W1 範例 3：字串格式化 (f-string)
學習重點：f-string 的使用
"""

# 基本資料
name = "小明"
age = 16
school = "內湖高工"

# 使用 f-string
print(f"我是 {name}，今年 {age} 歲")
print(f"我就讀於 {school}")
print(f"明年我就 {age + 1} 歲了")
print()

# 無人機參數
height = 0.5
speed = 0.3
distance = 10

print("===== 無人機飛行參數 =====")
print(f"高度：{height} 公尺")
print(f"速度：{speed} m/s")
print(f"距離：{distance} 公尺")
print(f"預估時間：{distance / speed:.2f} 秒")
print()

# 格式化數字
pi = 3.14159265359

print("圓周率的不同精度：")
print(f"完整：{pi}")
print(f"小數點後 2 位：{pi:.2f}")
print(f"小數點後 4 位：{pi:.4f}")
