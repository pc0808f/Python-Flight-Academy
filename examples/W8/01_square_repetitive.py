"""
W8 範例 1：正方形路徑（重複代碼版）
學習重點：體驗程式碼重複的冗贅感
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
print("  正方形路徑飛行")
print("=" * 50)

VELOCITY = 55
MOVE_TIME = 1.0  # 每邊飛行時間
TURN_TIME = 0.8  # 90 度轉彎時間

# 起飛
print("\n🚁 起飛中...")
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(2.0)
print("  ✓ 穩定懸停")
time.sleep(1.0)

print("\n開始正方形飛行...")

# 第一邊
print("\n第 1 邊：向前")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(MOVE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  轉彎 1：右轉 90°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# 第二邊
print("\n第 2 邊：向前")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(MOVE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  轉彎 2：右轉 90°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# 第三邊
print("\n第 3 邊：向前")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(MOVE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  轉彎 3：右轉 90°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# 第四邊
print("\n第 4 邊：向前")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(MOVE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  轉彎 4：右轉 90°（回到原始方向）")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# 降落
print("\n🛬 降落中...")
for motor in motors:
    motor.setVelocity(0)
time.sleep(3)

print("\n✅ 正方形飛行完成！")
print("=" * 50)
print("\n💭 思考問題：")
print("  1. 你發現程式碼有什麼問題嗎？")
print("  2. 如果要改變邊長，需要修改幾個地方？")
print("  3. 如果要畫八邊形，程式碼會有多長？")
print("  4. 有沒有更聰明的寫法？")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
