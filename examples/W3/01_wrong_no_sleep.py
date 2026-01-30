"""
W3 錯誤範例：沒有 sleep 的後果
學習重點：理解為什麼需要 time.sleep()
"""

from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())

# 取得馬達
m1 = drone.getDevice("m1_motor")
m2 = drone.getDevice("m2_motor")
m3 = drone.getDevice("m3_motor")
m4 = drone.getDevice("m4_motor")

# 設定模式
m1.setPosition(float('inf'))
m2.setPosition(float('inf'))
m3.setPosition(float('inf'))
m4.setPosition(float('inf'))

# ❌ 錯誤：起飛後立刻降落，沒有等待
print("起飛！")
m1.setVelocity(55)
m2.setVelocity(55)
m3.setVelocity(55)
m4.setVelocity(55)

print("降落！")  # 馬上就降落了！
m1.setVelocity(0)
m2.setVelocity(0)
m3.setVelocity(0)
m4.setVelocity(0)

# 結果：無人機幾乎沒有動作
# 因為指令執行太快，來不及完成動作

while drone.step(timestep) != -1:
    pass
