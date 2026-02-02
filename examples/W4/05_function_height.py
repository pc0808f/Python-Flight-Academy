"""
W4 範例 5：使用函數控制高度
學習重點：函數封裝與參數預設值
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

# 定義飛行函數
def fly_to_height(flight_time, velocity=55):
    """
    飛行到指定高度

    參數：
        flight_time: 飛行時間（秒）
        velocity: 馬達轉速（預設 55）
    """
    print(f"  ▲ 飛行 {flight_time} 秒（轉速 {velocity}）")

    for motor in motors:
        motor.setVelocity(velocity)

    time.sleep(flight_time)

def land():
    """降落"""
    print("  🛬 降落中...")
    for motor in motors:
        motor.setVelocity(0)

print("=" * 50)
print("  使用函數的階梯飛行")
print("=" * 50)

# 第一層
print("\n第一層：")
fly_to_height(1)  # 使用預設轉速
print("  📍 到達第一層")
time.sleep(1)

# 第二層
print("\n第二層：")
fly_to_height(1)  # 再飛 1 秒
print("  📍 到達第二層")
time.sleep(1)

# 第三層
print("\n第三層：")
fly_to_height(1, 60)  # 使用較高轉速
print("  📍 到達第三層（最高點）")
time.sleep(2)

# 降落
print()
land()
time.sleep(3)

print("\n✅ 飛行完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
