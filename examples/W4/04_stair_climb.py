"""
W4 範例 4：階梯式高度飛行
學習重點：使用參數控制不同高度
"""

import time
from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())

# 初始化馬達
motors = []
for i in range(1, 5):
    motor = drone.getDevice(f"m{i}_motor")
    motor.setPosition(float('inf'))
    motor.setVelocity(0)
    motors.append(motor)

# 定義三個高度（用飛行時間表示）
height_1 = 1.0  # 第一層（1 秒）
height_2 = 2.0  # 第二層（2 秒）
height_3 = 3.0  # 第三層（3 秒）

# 馬達轉速
velocity = 55

print("=" * 50)
print("  階梯式高度飛行")
print("=" * 50)

# 起飛到第一層
print(f"\n🚀 第一層：起飛 {height_1} 秒")
for motor in motors:
    motor.setVelocity(velocity)
time.sleep(height_1)
print("  📍 到達第一層")
time.sleep(1)  # 在這層停留 1 秒

# 上升到第二層
additional_time = height_2 - height_1
print(f"\n⬆️  第二層：再飛 {additional_time} 秒")
time.sleep(additional_time)
print("  📍 到達第二層")
time.sleep(1)

# 上升到第三層
additional_time = height_3 - height_2
print(f"\n⬆️  第三層：再飛 {additional_time} 秒")
time.sleep(additional_time)
print("  📍 到達第三層（最高點）")
time.sleep(2)

# 降落
print("\n🛬 開始降落...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("✅ 階梯飛行完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
