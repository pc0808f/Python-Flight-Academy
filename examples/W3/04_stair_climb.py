"""
W3 範例 4：階梯式上升
學習重點：分段控制飛行高度
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

print("=" * 40)
print("  階梯式上升飛行")
print("=" * 40)

# 第一段：起飛至低空
print("\n第一段：起飛至低空")
for motor in motors:
    motor.setVelocity(55)
time.sleep(1)
print("  📍 到達第一層")
time.sleep(1)

# 第二段：上升至中空
print("\n第二段：上升至中空")
time.sleep(1)
print("  📍 到達第二層")
time.sleep(1)

# 第三段：上升至高空
print("\n第三段：上升至高空")
time.sleep(1)
print("  📍 到達第三層（最高點）")
time.sleep(2)

# 開始下降
print("\n開始下降...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 階梯飛行完成！")
print("=" * 40)

while drone.step(timestep) != -1:
    pass
