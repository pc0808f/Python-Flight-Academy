"""
W8 範例 2：良好註解的正方形程式
學習重點：清晰的註解風格、程式碼組織

本程式展示如何撰寫易讀、易維護的飛行程式。
使用分段註解和常數定義，讓程式結構清晰。
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

# ========================================
#  飛行參數設定
# ========================================
BASE_VELOCITY = 55       # 基礎懸停速度
SIDE_LENGTH_TIME = 1.0   # 正方形每邊飛行時間（秒）
TURN_ANGLE_TIME = 0.8    # 90 度轉彎所需時間（秒）
NUM_SIDES = 4            # 正方形邊數

# 速度微調參數（用於前進和旋轉）
FORWARD_SPEED_DIFF = 10  # 前進時的速度差
TURN_SPEED_DIFF = 5      # 旋轉時的速度差

print("=" * 50)
print("  正方形路徑飛行（良好註解版）")
print("=" * 50)
print(f"\n飛行參數：")
print(f"  邊長：{SIDE_LENGTH_TIME}m")
print(f"  邊數：{NUM_SIDES}")
print(f"  總轉彎：{NUM_SIDES} 次")
print("=" * 50)

# ========================================
#  起飛階段
# ========================================
print("\n【階段 1】起飛")
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(2.0)
print("  ✓ 到達穩定高度")
time.sleep(1.0)

# ========================================
#  正方形飛行 - 第一邊
# ========================================
print("\n【階段 2】正方形飛行")
print("\n第 1 邊：向前（初始方向：北）")

# 前進動作：前方馬達減速，後方馬達加速
motors[0].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)  # 左前
motors[1].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)  # 右前
motors[2].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)  # 左後
motors[3].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)  # 右後
time.sleep(SIDE_LENGTH_TIME)

# 恢復懸停姿態
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)  # 穩定停頓

# 右轉 90 度（順時針）
print("  轉彎 1：右轉 90° → 朝向東")
motors[0].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
time.sleep(TURN_ANGLE_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

# ========================================
#  正方形飛行 - 第二邊
# ========================================
print("\n第 2 邊：向前（當前方向：東）")
motors[0].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
time.sleep(SIDE_LENGTH_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

print("  轉彎 2：右轉 90° → 朝向南")
motors[0].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
time.sleep(TURN_ANGLE_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

# ========================================
#  正方形飛行 - 第三邊
# ========================================
print("\n第 3 邊：向前（當前方向：南）")
motors[0].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
time.sleep(SIDE_LENGTH_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

print("  轉彎 3：右轉 90° → 朝向西")
motors[0].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
time.sleep(TURN_ANGLE_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

# ========================================
#  正方形飛行 - 第四邊
# ========================================
print("\n第 4 邊：向前（當前方向：西）")
motors[0].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY - FORWARD_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY + FORWARD_SPEED_DIFF)
time.sleep(SIDE_LENGTH_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

print("  轉彎 4：右轉 90° → 回到北（原始方向）")
motors[0].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
motors[1].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[2].setVelocity(BASE_VELOCITY + TURN_SPEED_DIFF)
motors[3].setVelocity(BASE_VELOCITY - TURN_SPEED_DIFF)
time.sleep(TURN_ANGLE_TIME)
for motor in motors:
    motor.setVelocity(BASE_VELOCITY)
time.sleep(0.5)

# ========================================
#  降落階段
# ========================================
print("\n【階段 3】降落")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 飛行任務完成！")
print("=" * 50)
print("\n📝 註解風格重點：")
print("  1. 使用分段註解（====）標記程式結構")
print("  2. 常數使用大寫命名（如 BASE_VELOCITY）")
print("  3. 每個動作都有清晰的說明")
print("  4. 標記當前朝向，幫助理解")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
