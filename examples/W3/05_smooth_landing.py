"""
W3 範例 5：平穩降落
學習重點：逐步降低轉速實現平穩降落
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

print("=" * 50)
print("  平穩降落示範")
print("=" * 50)

# 起飛
print("\n🚀 起飛中...")
for motor in motors:
    motor.setVelocity(55)
time.sleep(3)

# 懸停
print("✈️  到達目標高度，懸停中...")
time.sleep(2)

# 開始平穩降落
print("\n開始平穩降落...")
print("逐步降低馬達轉速...")

landing_speeds = [40, 30, 20, 10, 0]

for speed in landing_speeds:
    print(f"  降低轉速至 {speed:2d} → ", end="")

    for motor in motors:
        motor.setVelocity(speed)

    if speed == 0:
        print("著陸 🛬")
    else:
        print(f"高度下降中")

    time.sleep(0.8)

print("\n✅ 平穩降落完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
