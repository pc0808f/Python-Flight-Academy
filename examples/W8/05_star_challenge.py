"""
W8 範例 5：五角星形挑戰
學習重點：超級挑戰 - 複雜路徑規劃
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
print("  ⭐ 五角星形飛行挑戰")
print("=" * 50)

# ========== 飛行參數 ==========
VELOCITY = 55
SIDE_TIME = 1.0      # 每條星芒飛行時間
TURN_TIME = 1.8      # 144 度轉彎時間（大角度）

# 五角星幾何
NUM_POINTS = 5
TURN_ANGLE = 144     # 五角星的外角（360° / 5 × 2）

print(f"\n五角星幾何參數：")
print(f"  星芒數：{NUM_POINTS}")
print(f"  轉彎角度：{TURN_ANGLE}°")
print(f"  原理：跳過相鄰頂點，連接每隔一個頂點")
print("\n路徑示意（簡化）：")
print("        ★")
print("       / \\")
print("      /   \\")
print("     *     *")
print("      \\   /")
print("       \\ /")
print("        *")
print("\n⚠️  這是最困難的挑戰！")
print("=" * 50)

# ========== 起飛 ==========
print("\n🚁 起飛中...")
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(2.0)
time.sleep(1.0)

print("\n開始五角星飛行...")

# ========== 第一條星芒 ==========
print("\n第 1 條星芒 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 144°（大角度）")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第二條星芒 ==========
print("\n第 2 條星芒 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 144°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第三條星芒 ==========
print("\n第 3 條星芒 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 144°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第四條星芒 ==========
print("\n第 4 條星芒 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 144°")
motors[0].setVelocity(VELOCITY - 5)
motors[1].setVelocity(VELOCITY + 5)
motors[2].setVelocity(VELOCITY + 5)
motors[3].setVelocity(VELOCITY - 5)
time.sleep(TURN_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

# ========== 第五條星芒 ==========
print("\n第 5 條星芒 / 5")
motors[0].setVelocity(VELOCITY - 10)
motors[1].setVelocity(VELOCITY - 10)
motors[2].setVelocity(VELOCITY + 10)
motors[3].setVelocity(VELOCITY + 10)
time.sleep(SIDE_TIME)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)

print("  🔄 右轉 144°（回到起點）")
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

print("\n✅ ⭐ 五角星飛行完成！")
print("=" * 50)
print("\n🎉 恭喜你完成最困難的挑戰！")
print("\n📐 數學驗證：")
print(f"  總旋轉角度：144° × 5 = 720°")
print(f"  剛好旋轉兩圈（2 × 360°）")
print("\n🌟 五角星的秘密：")
print("  - 不是畫五邊形（72° × 5 = 360°）")
print("  - 而是跳躍連接（144° × 5 = 720°）")
print("  - 每次跳過一個頂點，形成星形")
print("\n💡 公式：")
print("  五角星轉角 = 360° / 5 × 2 = 144°")
print("  N 角星轉角 = 360° / N × 2")
print("=" * 50)
print("\n✨ 你已經掌握了複雜路徑規劃！")
print("   下週我們將學習如何用「迴圈」讓程式變短！")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
