"""
W3 範例 2：基礎起飛與降落
學習重點：使用 time.sleep() 控制飛行時間
"""

import time
from controller import Robot

# 初始化
drone = Robot()
timestep = int(drone.getBasicTimeStep())

# 取得四個馬達
m1_motor = drone.getDevice("m1_motor")
m2_motor = drone.getDevice("m2_motor")
m3_motor = drone.getDevice("m3_motor")
m4_motor = drone.getDevice("m4_motor")

# 設定馬達為速度控制模式
m1_motor.setPosition(float('inf'))
m2_motor.setPosition(float('inf'))
m3_motor.setPosition(float('inf'))
m4_motor.setPosition(float('inf'))

# 初始化馬達速度為 0
m1_motor.setVelocity(0)
m2_motor.setVelocity(0)
m3_motor.setVelocity(0)
m4_motor.setVelocity(0)

print("=" * 40)
print("  基礎起飛與降落")
print("=" * 40)

# 起飛
print("🚀 起飛中...")
m1_motor.setVelocity(55)
m2_motor.setVelocity(55)
m3_motor.setVelocity(55)
m4_motor.setVelocity(55)

time.sleep(2)  # 等待 2 秒，讓無人機上升

# 懸停
print("✈️  懸停中...")
time.sleep(3)  # 懸停 3 秒

# 降落
print("🛬 降落中...")
m1_motor.setVelocity(0)
m2_motor.setVelocity(0)
m3_motor.setVelocity(0)
m4_motor.setVelocity(0)

time.sleep(2)  # 等待 2 秒，讓無人機降落

print("✅ 飛行任務完成！")
print("=" * 40)

# 主迴圈
while drone.step(timestep) != -1:
    pass
