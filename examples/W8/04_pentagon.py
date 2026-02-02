"""
W8 範例 4：正五邊形路徑
學習重點：體驗更多邊數的重複痛苦
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
print("  正五邊形路徑飛行")
print("=" * 50)

# ========== 飛行參數 ==========
VELOCITY = 55
SIDE_TIME = 0.8      # 每邊飛行時間（縮短一點）
TURN_TIME = 0.9      # 72 度轉彎時間

# 幾何參數
NUM_SIDES = 5
EXTERIOR_ANGLE = 360 / NUM_SIDES  # 72°

print(f"\n五邊形幾何參數：")
print(f"  邊數：{NUM_SIDES}")
print(f"  外角：{EXTERIOR_ANGLE}°")
print(f"  內角：{180 - EXTERIOR_ANGLE}°")
print("\n⚠️  警告：這個程式有 20 行重複的程式碼！")
print("=" * 50)

# ========== 起飛 ==========
print("\n🚁 起飛中...")
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(2.0)
time.sleep(1.0)

print("\n開始五邊形飛行...")

# ========== 第一邊 ==========
print("\n第 1 邊 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

print("  🔄 右轉 72°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

# ========== 第二邊 ==========
print("\n第 2 邊 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

print("  🔄 右轉 72°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

# ========== 第三邊 ==========
print("\n第 3 邊 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

print("  🔄 右轉 72°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

# ========== 第四邊 ==========
print("\n第 4 邊 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

print("  🔄 右轉 72°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

# ========== 第五邊 ==========
print("\n第 5 邊 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

print("  🔄 右轉 72°（回到起點）")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.4)

# ========== 降落 ==========
print("\n🛬 降落中...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 五邊形飛行完成！")
print("=" * 50)
print("\n😫 累了嗎？讓我們統計一下：")
print(f"  程式總行數：約 140 行")
print(f"  重複的程式碼段：5 組")
print(f"  每組行數：約 16 行")
print(f"  重複行數：約 80 行")
print("\n💭 想像一下：")
print("  如果畫十邊形：160 行重複代碼")
print("  如果畫圓形（36 邊形）：超過 500 行！")
print("\n💡 問題：")
print("  有沒有更聰明的方法來處理重複的程式碼？")
print("  提示：下週會學習一個神奇的工具叫做「迴圈」")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
