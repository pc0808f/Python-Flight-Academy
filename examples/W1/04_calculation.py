"""
W1 範例 4：算術運算
學習重點：基本運算子的使用
"""

# 基本運算
a = 10
b = 3

print("===== 基本運算 =====")
print(f"{a} + {b} = {a + b}")      # 加法
print(f"{a} - {b} = {a - b}")      # 減法
print(f"{a} * {b} = {a * b}")      # 乘法
print(f"{a} / {b} = {a / b:.2f}")  # 除法
print()

# 特殊運算
print("===== 特殊運算 =====")
print(f"{a} // {b} = {a // b}")    # 整數除法
print(f"{a} % {b} = {a % b}")      # 取餘數
print(f"{a} ** {b} = {a ** b}")    # 次方
print()

# 飛行計算範例
print("===== 飛行計算 =====")
speed = 0.5      # 速度：m/s
time = 10        # 時間：秒

distance = speed * time
print(f"速度：{speed} m/s")
print(f"時間：{time} 秒")
print(f"飛行距離：{distance} 公尺")
print()

# 反向計算
target_distance = 20  # 目標距離
flight_time = target_distance / speed
print(f"目標距離：{target_distance} 公尺")
print(f"所需時間：{flight_time} 秒")
