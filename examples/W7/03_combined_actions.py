"""
W7 範例 3：組合動作序列
學習重點：連續動作、停頓穩定
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
print("  組合動作序列示範")
print("=" * 50)

# 定義基本動作函數
def takeoff(duration=2.0, velocity=55):
    """起飛"""
    print("  🚁 起飛中...")
    for motor in motors:
        motor.setVelocity(velocity)
    time.sleep(duration)
    print("  ✓ 到達穩定高度")

def hover(duration):
    """懸停"""
    print(f"  ⏸️  懸停 {duration} 秒")
    time.sleep(duration)

def move_forward(duration, velocity=55):
    """前進"""
    print(f"  ➡️  前進 {duration} 秒")
    # 前進：前方馬達減速，後方馬達加速
    motors[0].setVelocity(velocity - 10)  # 左前
    motors[1].setVelocity(velocity - 10)  # 右前
    motors[2].setVelocity(velocity + 10)  # 左後
    motors[3].setVelocity(velocity + 10)  # 右後
    time.sleep(duration)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(velocity)

def rotate_right(duration=0.8, velocity=55):
    """右轉（順時針）90 度"""
    print("  🔄 右轉 90°")
    motors[0].setVelocity(velocity - 5)   # 左前（減速）
    motors[1].setVelocity(velocity + 5)   # 右前（加速）
    motors[2].setVelocity(velocity + 5)   # 左後（加速）
    motors[3].setVelocity(velocity - 5)   # 右後（減速）
    time.sleep(duration)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(velocity)

def land():
    """降落"""
    print("  🛬 降落中...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

# ========== 組合動作任務 ==========
print("\n【任務】前進 → 右轉 → 再前進")
print("=" * 50)

# 起飛
takeoff()
hover(1.0)

# 第一段：前進
print("\n步驟 1：向前移動")
move_forward(1.5)
hover(0.5)  # 停頓穩定

# 轉向
print("\n步驟 2：右轉 90 度")
rotate_right()
hover(0.5)  # 停頓穩定

# 第二段：前進
print("\n步驟 3：向前移動（新方向）")
move_forward(1.0)
hover(0.5)

# 降落
print("\n步驟 4：降落")
land()

print("\n✅ 組合動作完成！")
print("=" * 50)
print("\n重要觀念：")
print("  1. 每個動作後需要停頓（0.3-0.5 秒）")
print("  2. 停頓讓無人機姿態穩定")
print("  3. 組合動作 = 基本動作 + 停頓")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
