"""
W7 範例 5：Z 形路徑進階挑戰
學習重點：複雜路徑規劃、多次轉向
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
print("  Z 形路徑進階挑戰")
print("=" * 50)

# 飛行參數
VELOCITY = 55
SEGMENT_TIME = 1.2  # 每段直線時間
TURN_TIME = 0.8     # 90 度轉彎時間

# 動作函數
def takeoff():
    print("\n🚁 起飛中...")
    for motor in motors:
        motor.setVelocity(VELOCITY)
    time.sleep(2.0)
    print("  ✓ 穩定懸停")

def move_forward(duration):
    motors[0].setVelocity(VELOCITY - 10)
    motors[1].setVelocity(VELOCITY - 10)
    motors[2].setVelocity(VELOCITY + 10)
    motors[3].setVelocity(VELOCITY + 10)
    time.sleep(duration)
    for motor in motors:
        motor.setVelocity(VELOCITY)

def rotate_left_90():
    """左轉 90 度（逆時針）"""
    motors[0].setVelocity(VELOCITY + 5)
    motors[1].setVelocity(VELOCITY - 5)
    motors[2].setVelocity(VELOCITY - 5)
    motors[3].setVelocity(VELOCITY + 5)
    time.sleep(TURN_TIME)
    for motor in motors:
        motor.setVelocity(VELOCITY)

def rotate_right_90():
    """右轉 90 度（順時針）"""
    motors[0].setVelocity(VELOCITY - 5)
    motors[1].setVelocity(VELOCITY + 5)
    motors[2].setVelocity(VELOCITY + 5)
    motors[3].setVelocity(VELOCITY - 5)
    time.sleep(TURN_TIME)
    for motor in motors:
        motor.setVelocity(VELOCITY)

def land():
    print("\n🛬 降落中...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

# ========== Z 形路徑飛行 ==========
print("\n路徑示意圖：")
print("  起點 →→→ A")
print("        ↙︎")
print("      ↙︎")
print("    B →→→ 終點")
print()

# 起飛
takeoff()
time.sleep(1.0)

# 第一段：水平線（Z 的上橫）
print("\n【步驟 1】第一段水平線")
print("  ➡️  向右前進...")
move_forward(SEGMENT_TIME)
time.sleep(0.5)
print("  ✓ 到達 A 點")

# 第一次轉向：右轉 135 度（轉成斜向左下）
# 因為 Z 的斜線，需要轉更大的角度
print("\n【步驟 2】右轉 135 度（斜向）")
print("  🔄 轉向中...")
rotate_right_90()
time.sleep(0.1)
rotate_right_90()  # 再轉 45 度（用一半時間）
time.sleep(TURN_TIME * 0.5)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)
print("  ✓ 轉向完成")

# 第二段：斜線（Z 的斜邊）
print("\n【步驟 3】斜線段")
print("  ➡️  斜向前進...")
move_forward(SEGMENT_TIME * 1.4)  # 斜線較長
time.sleep(0.5)
print("  ✓ 到達 B 點")

# 第二次轉向：左轉 135 度（轉回水平向右）
print("\n【步驟 4】左轉 135 度（回到水平）")
print("  🔄 轉向中...")
rotate_left_90()
time.sleep(0.1)
rotate_left_90()
time.sleep(TURN_TIME * 0.5)
for motor in motors:
    motor.setVelocity(VELOCITY)
time.sleep(0.5)
print("  ✓ 轉向完成")

# 第三段：水平線（Z 的下橫）
print("\n【步驟 5】第三段水平線")
print("  ➡️  向右前進...")
move_forward(SEGMENT_TIME)
time.sleep(0.5)
print("  ✓ 到達終點")

# 降落
land()

print("\n✅ Z 形路徑飛行完成！")
print("=" * 50)
print("\n飛行統計：")
print("  直線段數：3 段")
print("  轉彎次數：2 次")
print("  轉彎角度：135° × 2")
print("  總飛行時間：約 15 秒")
print("=" * 50)
print("\n💡 進階思考：")
print("  - Z 形需要多次大角度轉彎")
print("  - 斜線段的距離較長（√2 倍）")
print("  - 兩次轉向方向相反才能閉合路徑")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
