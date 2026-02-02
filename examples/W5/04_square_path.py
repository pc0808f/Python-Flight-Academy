"""
W5 範例 4：正方形路徑
學習重點：使用迴圈飛出正方形
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
    for motor in motors:
        motor.setVelocity(55)
    time.sleep(2)

def land():
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

def move(direction, distance):
    print(f"  {direction}")
    time.sleep(distance)

print("=" * 50)
print("  正方形路徑飛行")
print("=" * 50)

takeoff()

# 正方形的四個邊
corners = ["(0,0)", "(1,0)", "(1,1)", "(0,1)", "(0,0)"]
directions = ["→ 向右", "↑ 向前", "← 向左", "↓ 向後"]

for i in range(4):
    print(f"\n第 {i+1} 邊：從 {corners[i]} 到 {corners[i+1]}")
    move(directions[i], 1)
    print(f"  📍 到達 {corners[i+1]}")
    time.sleep(0.5)  # 在角落停留

land()

print("\n✅ 正方形路徑完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
