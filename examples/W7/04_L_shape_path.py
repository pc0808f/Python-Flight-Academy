"""
W7 範例 4：L 形路徑飛行
學習重點：路徑規劃、組合動作應用
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
print("  L 形路徑飛行挑戰")
print("=" * 50)

# 飛行參數
FLIGHT_VELOCITY = 55
HORIZONTAL_DISTANCE = 1.5  # 水平段距離（秒）
VERTICAL_DISTANCE = 1.0    # 垂直段距離（秒）
TURN_TIME = 0.8            # 90 度轉彎時間

# 定義動作函數
def takeoff(duration=2.0):
    """起飛到穩定高度"""
    print("\n🚁 起飛中...")
    for motor in motors:
        motor.setVelocity(FLIGHT_VELOCITY)
    time.sleep(duration)
    print("  ✓ 到達穩定高度")

def hover(duration):
    """懸停穩定"""
    time.sleep(duration)

def move_forward(duration):
    """向前移動"""
    motors[0].setVelocity(FLIGHT_VELOCITY - 10)
    motors[1].setVelocity(FLIGHT_VELOCITY - 10)
    motors[2].setVelocity(FLIGHT_VELOCITY + 10)
    motors[3].setVelocity(FLIGHT_VELOCITY + 10)
    time.sleep(duration)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(FLIGHT_VELOCITY)

def rotate_right_90():
    """右轉 90 度"""
    motors[0].setVelocity(FLIGHT_VELOCITY - 5)
    motors[1].setVelocity(FLIGHT_VELOCITY + 5)
    motors[2].setVelocity(FLIGHT_VELOCITY + 5)
    motors[3].setVelocity(FLIGHT_VELOCITY - 5)
    time.sleep(TURN_TIME)
    # 恢復懸停
    for motor in motors:
        motor.setVelocity(FLIGHT_VELOCITY)

def land():
    """降落"""
    print("\n🛬 降落中...")
    for motor in motors:
        motor.setVelocity(0)
    time.sleep(3)

# ========== L 形路徑飛行 ==========
print("\n路徑示意圖：")
print("  起點 →→→→ A 點")
print("          ↓")
print("          ↓")
print("          B 點（終點）")
print()

# 起飛
takeoff()
hover(1.0)

# 步驟 1：水平段
print("\n【步驟 1】水平段（向前 1.5m）")
print("  ➡️  前進中...")
move_forward(HORIZONTAL_DISTANCE)
hover(0.5)
print("  ✓ 到達 A 點")

# 步驟 2：轉向
print("\n【步驟 2】右轉 90 度")
print("  🔄 旋轉中...")
rotate_right_90()
hover(0.5)
print("  ✓ 轉向完成")

# 步驟 3：垂直段
print("\n【步驟 3】垂直段（向前 1.0m）")
print("  ➡️  前進中...")
move_forward(VERTICAL_DISTANCE)
hover(0.5)
print("  ✓ 到達 B 點（終點）")

# 降落
land()

print("\n✅ L 形路徑飛行完成！")
print("=" * 50)
print("\n飛行統計：")
print(f"  水平段：{HORIZONTAL_DISTANCE} 公尺")
print(f"  垂直段：{VERTICAL_DISTANCE} 公尺")
print(f"  總轉彎：1 次（90 度）")
print("=" * 50)

while drone.step(timestep) != -1:
    pass
