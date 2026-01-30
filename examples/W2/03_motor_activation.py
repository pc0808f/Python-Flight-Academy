"""
W2 範例 3：啟動馬達
學習重點：取得裝置物件並控制馬達
"""

from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())

# 取得四個馬達裝置
m1_motor = drone.getDevice("m1_motor")
m2_motor = drone.getDevice("m2_motor")
m3_motor = drone.getDevice("m3_motor")
m4_motor = drone.getDevice("m4_motor")

print("✅ 已取得 4 個馬達")

# 設定馬達為速度控制模式
m1_motor.setPosition(float('inf'))
m2_motor.setPosition(float('inf'))
m3_motor.setPosition(float('inf'))
m4_motor.setPosition(float('inf'))

print("✅ 馬達模式設定完成")

# 設定馬達轉速（較小的值，避免翻覆）
velocity = 10.0
m1_motor.setVelocity(velocity)
m2_motor.setVelocity(velocity)
m3_motor.setVelocity(velocity)
m4_motor.setVelocity(velocity)

print(f"✅ 馬達轉速設定為 {velocity}")
print("🚀 馬達啟動！觀察無人機的反應...")

step_count = 0

while drone.step(timestep) != -1:
    step_count += 1

    # 執行 200 步後停止
    if step_count >= 200:
        # 停止馬達
        m1_motor.setVelocity(0)
        m2_motor.setVelocity(0)
        m3_motor.setVelocity(0)
        m4_motor.setVelocity(0)
        print("⏹️  馬達已停止")
        break
