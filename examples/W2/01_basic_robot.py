"""
W2 範例 1：基本 Robot 物件
學習重點：建立 Robot 物件並取得基本資訊
"""

from controller import Robot

# 建立機器人物件
drone = Robot()
print("✈️ 無人機物件已建立！")

# 取得基本資訊
name = drone.getName()
timestep = int(drone.getBasicTimeStep())

print(f"🏷️  無人機名稱：{name}")
print(f"⏱️  時間步長：{timestep} ms")

# 主迴圈
print("🚀 模擬開始...")

while drone.step(timestep) != -1:
    # 目前什麼都不做，只是讓模擬運行
    pass
