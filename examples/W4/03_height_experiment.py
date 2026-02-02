"""
W4 範例 3：高度實驗程式
學習重點：測試不同轉速的飛行效果
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

# 測試不同轉速
test_velocities = [45, 50, 55, 60, 65]

print("=" * 50)
print("  轉速與高度關係實驗")
print("=" * 50)

for vel in test_velocities:
    print(f"\n🔬 測試轉速：{vel}")

    # 起飛
    for motor in motors:
        motor.setVelocity(vel)

    print(f"  ▲ 上升中...")
    time.sleep(2)  # 飛行 2 秒
    print(f"  📏 請觀察並記錄高度")

    # 降落
    for motor in motors:
        motor.setVelocity(0)

    print(f"  ▼ 降落中...")
    time.sleep(3)  # 等待完全降落

    if vel < test_velocities[-1]:
        print("  ⏸️  按 Enter 繼續下一個測試...")
        # input()  # 在實際使用時可取消註解

while drone.step(timestep) != -1:
    pass

print("\n✅ 實驗完成！")
print("=" * 50)
