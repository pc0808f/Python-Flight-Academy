"""
W2 範例 4：創意啟動畫面
學習重點：字串格式化與美化輸出
"""

from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())
name = drone.getName()

# 創意啟動畫面
print("=" * 50)
print("    ✈️  飛行驅動 Python 模擬器  ✈️")
print("=" * 50)
print(f"無人機型號：{name}")
print(f"時間步長：{timestep} ms")
print("系統狀態：✅ 正常")
print("電池電量：🔋🔋🔋🔋🔋 100%")
print("GPS 定位：📍 已就緒")
print("=" * 50)
print("準備起飛...")
print("=" * 50)

step_count = 0
status_updates = [100, 200, 300, 400, 500]

while drone.step(timestep) != -1:
    step_count += 1

    # 在特定步數顯示狀態更新
    if step_count in status_updates:
        progress = (step_count / 500) * 100
        print(f"系統檢查進度：{progress:.0f}%")

    if step_count >= 500:
        break

print("=" * 50)
print("✅ 系統檢查完成，準備就緒！")
print("=" * 50)
