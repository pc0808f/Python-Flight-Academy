"""
W6 範例 3：累加器模式
學習重點：累積數值
"""

import time

# 距離累加器
total_distance = 0

print("===== 飛行距離累積 =====\n")

flights = [1.5, 2.0, 1.0, 2.5, 1.8]

for i, distance in enumerate(flights, 1):
    print(f"第 {i} 段飛行：{distance} 公尺")

    total_distance += distance

    print(f"  累計距離：{total_distance} 公尺")
    time.sleep(0.5)
    print()

print("=" * 40)
print(f"總飛行距離：{total_distance} 公尺")
print(f"平均距離：{total_distance / len(flights):.2f} 公尺")
print("=" * 40)
