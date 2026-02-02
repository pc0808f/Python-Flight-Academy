"""
W5 範例 5：字母 L 路徑
學習重點：設計自訂飛行路徑
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
    print("🚀 起飛...")
    for motor in motors:
        motor.setVelocity(55)
    time.sleep(2)

def land():
    print("🛬 降落...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

def move_to(x, y):
    """移動到座標（模擬）"""
    print(f"  移動到 ({x}, {y})")
    # 簡化：用總時間表示
    total_time = abs(x) + abs(y)
    time.sleep(total_time * 0.5)

print("=" * 50)
print("  字母 L 路徑飛行")
print("=" * 50)
print("\n路徑：(0,0) → (2,0) → (2,2)\n")

takeoff()

# 起點
current = (0, 0)
print(f"📍 起點：{current}")

# 底部橫線
print("\n1. 畫底部橫線")
current = (2, 0)
move_to(2, 0)
print(f"  ✓ 到達：{current}")
time.sleep(1)

# 垂直線
print("\n2. 畫垂直線")
current = (2, 2)
move_to(0, 2)
print(f"  ✓ 到達：{current}")
time.sleep(1)

land()

print("\n✅ 字母 L 完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
