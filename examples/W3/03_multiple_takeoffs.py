"""
W3 範例 3：連續起降
學習重點：使用 for 迴圈實現重複飛行
"""

import time
from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())

# 取得馬達並設定（省略重複代碼）
motors = []
for i in range(1, 5):
    motor = drone.getDevice(f"m{i}_motor")
    motor.setPosition(float('inf'))
    motor.setVelocity(0)
    motors.append(motor)

print("=" * 40)
print("  連續起降任務")
print("=" * 40)

# 連續起降 3 次
for lap in range(3):
    print(f"\n第 {lap + 1} 次起飛")

    # 起飛
    print("  🚀 起飛中...")
    for motor in motors:
        motor.setVelocity(55)
    time.sleep(2)

    # 懸停
    print("  ✈️  懸停中...")
    time.sleep(2)

    # 降落
    print("  🛬 降落中...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(2)

    # 等待下一次起飛
    if lap < 2:  # 最後一次不用等待
        print("  ⏸️  等待 1 秒...")
        time.sleep(1)

print("\n✅ 所有飛行任務完成！")
print("=" * 40)

while drone.step(timestep) != -1:
    pass
