"""
W4 範例 2：整數 vs 浮點數
學習重點：理解兩種數值型態的差異
"""

print("===== 整數（Integer）=====")
age = 16
count = 30
print(f"年齡：{age}（型態：{type(age)}）")
print(f"數量：{count}（型態：{type(count)}）")

print("\n===== 浮點數（Float）=====")
height = 1.75
speed = 0.5
print(f"身高：{height}（型態：{type(height)}）")
print(f"速度：{speed}（型態：{type(speed)}）")

print("\n===== 運算結果 =====")
# 整數運算
a = 10
b = 3
print(f"{a} / {b} = {a / b}（浮點數）")
print(f"{a} // {b} = {a // b}（整數除法）")
print(f"{a} % {b} = {a % b}（取餘數）")

print("\n===== 混合運算 =====")
# 整數 + 浮點數 = 浮點數
x = 5      # 整數
y = 2.5    # 浮點數
z = x + y  # 結果是浮點數
print(f"{x} + {y} = {z}")
print(f"結果型態：{type(z)}")

print("\n===== 飛行參數範例 =====")
flight_time = 2      # 整數（夠用了）
flight_time_precise = 2.5  # 浮點數（更精確）

print(f"飛行時間（整數）：{flight_time} 秒")
print(f"飛行時間（浮點數）：{flight_time_precise} 秒")
