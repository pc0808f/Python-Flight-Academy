"""
W2 範例 2：步數計數器
學習重點：while 迴圈與步數統計
"""

from controller import Robot

drone = Robot()
timestep = int(drone.getBasicTimeStep())

step_count = 0
max_steps = 500

print("開始計數...")

while drone.step(timestep) != -1:
    step_count += 1

    # 每 100 步輸出一次
    if step_count % 100 == 0:
        print(f"已執行 {step_count} 步")

    # 達到指定步數後結束
    if step_count >= max_steps:
        print("✅ 達到目標步數，結束模擬")
        break

# 計算總模擬時間
total_time = (step_count * timestep) / 1000  # 轉換為秒
print(f"\n總共執行 {step_count} 步")
print(f"總模擬時間 {total_time:.2f} 秒")
