"""
W5 範例 3：十字路徑
學習重點：組合多個移動指令
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

def takeoff():
    """起飛"""
    print("🚀 起飛...")
    for motor in motors:
        motor.setVelocity(55)
    time.sleep(2)

def land():
    """降落"""
    print("🛬 降落...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

def move(direction, distance):
    """移動（模擬）"""
    print(f"  {direction} 移動 {distance} 單位")
    time.sleep(distance)

print("=" * 50)
print("  十字路徑飛行")
print("=" * 50)

takeoff()

# 十字路徑
print("\n中心 → 前")
move("➡️", 1)
move("⬅️", 1)  # 回中心

print("\n中心 → 後")
move("⬅️", 1)
move("➡️", 1)  # 回中心

print("\n中心 → 右")
move("⬇️", 1)
move("⬆️", 1)  # 回中心

print("\n中心 → 左")
move("⬆️", 1)
move("⬇️", 1)  # 回中心

print()
land()

print("\n✅ 十字路徑完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
