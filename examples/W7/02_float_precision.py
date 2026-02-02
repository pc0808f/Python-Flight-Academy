"""
W7 範例 2：浮點數精確度問題
學習重點：認識浮點數誤差、round() 函數
"""

print("=" * 50)
print("  浮點數精確度實驗")
print("=" * 50)

# 實驗 1：簡單加法的誤差
print("\n【實驗 1】簡單加法")
print("-" * 40)

result = 0.1 + 0.2
print(f"0.1 + 0.2 = {result}")
print(f"結果是 0.3 嗎？ {result == 0.3}")
print(f"實際值：{result:.20f}")  # 顯示 20 位小數

# 實驗 2：累積誤差
print("\n【實驗 2】累積誤差")
print("-" * 40)

angle = 0.0
print(f"初始角度：{angle}")

for i in range(10):
    angle += 0.1
    print(f"第 {i+1} 次 +0.1：{angle:.15f}")

print(f"\n預期結果：1.0")
print(f"實際結果：{angle}")
print(f"是否等於 1.0？ {angle == 1.0}")

# 實驗 3：使用 round() 修正
print("\n【實驗 3】使用 round() 修正")
print("-" * 40)

angle = 0.0
for i in range(10):
    angle += 0.1
    angle = round(angle, 2)  # 四捨五入到 2 位小數
    print(f"第 {i+1} 次（修正後）：{angle}")

print(f"\n修正後是否等於 1.0？ {angle == 1.0}")

# 實驗 4：飛行應用範例
print("\n【實驗 4】飛行參數計算")
print("-" * 40)

# 模擬旋轉角度累積
total_rotation = 0.0
turn_angle = 90.0  # 每次轉 90 度

print("正方形飛行（4 次轉彎）：")
for i in range(4):
    total_rotation += turn_angle
    print(f"  轉彎 {i+1}：累積 {total_rotation}°")

print(f"\n預期總旋轉：360°")
print(f"實際總旋轉：{total_rotation}°")
print(f"是否回到原點？ {total_rotation == 360.0}")

# 實驗 5：容差範圍判斷
print("\n【實驗 5】容差範圍判斷法")
print("-" * 40)

measured_height = 1.0000001  # 模擬感測器讀值
target_height = 1.0

# 方法 1：直接比較（可能失敗）
print(f"直接比較：{measured_height == target_height}")

# 方法 2：容差範圍判斷
tolerance = 0.0001
is_close = abs(measured_height - target_height) < tolerance
print(f"容差判斷：{is_close}")
print(f"  誤差：{abs(measured_height - target_height):.10f}")

# 總結
print("\n" + "=" * 50)
print("  重要觀念")
print("=" * 50)
print("1. 浮點數運算會有微小誤差")
print("2. 不要用 == 直接比較浮點數")
print("3. 解決方法：")
print("   - 使用 round() 四捨五入")
print("   - 使用容差範圍判斷")
print("   - 盡量使用整數運算")
print("=" * 50)
