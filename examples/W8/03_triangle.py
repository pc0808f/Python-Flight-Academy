"""
W8 範例 3：等邊三角形路徑
學習重點：不同邊數的多邊形、外角計算
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
print("  等邊三角形路徑飛行")
print("=" * 50)

# ========== 飛行參數 ==========
VELOCITY = 55
SIDE_TIME = 1.2      # 每邊飛行時間
TURN_TIME = 1.2      # 120 度轉彎時間（比 90 度需要更長）

# 幾何知識
NUM_SIDES = 3
EXTERIOR_ANGLE = 360 / NUM_SIDES  # 外角 = 360° / 邊數 = 120°

print(f"\n三角形幾何參數：")
print(f"  邊數：{NUM_SIDES}")
print(f"  外角：{EXTERIOR_ANGLE}°")
print(f"  內角：{180 - EXTERIOR_ANGLE}°")
print("=" * 50)

# ========== 起飛 ==========
print("\n🚁 起飛中...")
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(2.0)
print("  ✓ 穩定懸停")
time.sleep(1.0)

print("\n開始三角形飛行...")

# ========== 第一邊 ==========
print("\n第 1 邊 / 3")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 120°（1/3）")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第二邊 ==========
print("\n第 2 邊 / 3")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 120°（2/3）")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第三邊 ==========
print("\n第 3 邊 / 3")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 120°（3/3）回到起點")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 降落 ==========
print("\n🛬 降落中...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 三角形飛行完成！")
print("=" * 50)
print("\n📐 數學驗證：")
print(f"  總旋轉角度：120° × 3 = 360°")
print(f"  ✓ 剛好旋轉一圈，回到原始方向")
print("\n💡 關鍵公式：")
print("  外角 = 360° / 邊數")
print("  三角形：360° / 3 = 120°")
print("  正方形：360° / 4 = 90°")
print("  五邊形：360° / 5 = 72°")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
