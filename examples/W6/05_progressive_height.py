"""
W6 範例 5：漸進式高度控制
學習重點：動態調整飛行參數
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
print("  漸進式高度上升")
print("=" * 50)

# 初始參數
flight_time = 0.5  # 起始飛行時間
increment = 0.3    # 每次增加的時間
velocity = 55

# 啟動馬達
for motor in motors:
    motor.setVelocity(velocity)

# 5 階漸進上升
total_time = 0

for level in range(1, 6):
    print(f"\n第 {level} 階：飛行 {flight_time:.1f} 秒")

    time.sleep(flight_time)
    total_time += flight_time

    print(f"  📍 到達第 {level} 階")
    print(f"  ⏱️  累計飛行：{total_time:.1f} 秒")

    # 每次增加飛行時間
    flight_time += increment

    time.sleep(0.5)  # 短暫停留

# 降落
print("\n🛬 開始降落...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print(f"\n✅ 漸進飛行完成！")
print(f"總飛行時間：{total_time:.1f} 秒")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
