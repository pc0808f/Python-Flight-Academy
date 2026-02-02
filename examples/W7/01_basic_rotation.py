"""
W7 範例 1：基本旋轉控制
學習重點：原地旋轉、時間與角度關係
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
print("  基本旋轉控制示範")
print("=" * 50)

# 起飛
print("\n🚁 起飛中...")
for motor in motors:
    motor.setVelocity(55)
time.sleep(2.0)
print("  ✓ 到達穩定高度")

# 停頓穩定
time.sleep(1.0)

# 旋轉函數定義
def rotate_clockwise(duration):
    """順時針旋轉"""
    motors[0].setVelocity(50)   # 左前（減速）
    motors[1].setVelocity(60)   # 右前（加速）
    motors[2].setVelocity(60)   # 左後（加速）
    motors[3].setVelocity(50)   # 右後（減速）
    time.sleep(duration)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(55)

def rotate_counterclockwise(duration):
    """逆時針旋轉"""
    motors[0].setVelocity(60)   # 左前（加速）
    motors[1].setVelocity(50)   # 右前（減速）
    motors[2].setVelocity(50)   # 左後（減速）
    motors[3].setVelocity(60)   # 右後（加速）
    time.sleep(duration)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(55)

# 第一次旋轉：順時針 90 度
print("\n🔄 順時針旋轉 90 度...")
rotate_clockwise(0.8)  # 實驗得出的時間參數
time.sleep(0.5)  # 穩定停頓
print("  ✓ 完成旋轉")

# 觀察停頓
print("\n⏸️  停頓觀察（2 秒）")
time.sleep(2.0)

# 第二次旋轉：逆時針 90 度（回正）
print("\n🔄 逆時針旋轉 90 度（回到原始方向）...")
rotate_counterclockwise(0.8)
time.sleep(0.5)
print("  ✓ 回到原始朝向")

# 最終停頓
time.sleep(1.0)

# 降落
print("\n🛬 開始降落...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 旋轉示範完成！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
