"""
W6 範例 2：計數器模式
學習重點：使用變數計數
"""

import time

# 起降計數器
takeoff_count = 0
landing_count = 0

print("===== 飛行計數器 =====\n")

for flight in range(1, 4):
    print(f"第 {flight} 次飛行：")

    # 起飛
    takeoff_count += 1
    print(f"  🚀 起飛（累計 {takeoff_count} 次）")
    time.sleep(1)

    # 降落
    landing_count += 1
    print(f"  🛬 降落（累計 {landing_count} 次）")
    time.sleep(1)
    print()

print("=" * 40)
print(f"總計：")
print(f"  起飛：{takeoff_count} 次")
print(f"  降落：{landing_count} 次")
print("=" * 40)
