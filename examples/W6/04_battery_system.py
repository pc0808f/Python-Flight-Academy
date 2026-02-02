"""
W6 範例 4：電池管理系統
學習重點：模擬電池消耗與管理
"""

import time

# 電池參數
battery = 100
warning_level = 30
critical_level = 15

print("=" * 50)
print("  電池管理系統")
print("=" * 50)

def check_battery():
    """檢查電池狀態"""
    if battery <= critical_level:
        print(f"  ⚠️  電量危險！({battery}%)")
        return "critical"
    elif battery <= warning_level:
        print(f"  ⚡ 電量偏低 ({battery}%)")
        return "warning"
    else:
        print(f"  ✅ 電量充足 ({battery}%)")
        return "normal"

def fly_mission(duration, consumption):
    """執行飛行任務"""
    global battery

    print(f"\n任務時長：{duration} 秒，消耗：{consumption}%")

    status = check_battery()

    if status == "critical":
        print("  ❌ 任務取消：電量不足")
        return False

    # 執行任務
    time.sleep(duration)
    battery -= consumption

    print(f"  ✓ 任務完成，剩餘電量：{battery}%")
    return True

# 模擬多次飛行
missions = [(2, 15), (3, 20), (2, 15), (2, 15), (2, 15), (2, 10)]

for i, (duration, consumption) in enumerate(missions, 1):
    print(f"\n{'='*50}")
    print(f"任務 {i}：")

    if not fly_mission(duration, consumption):
        print("\n⚠️  電量過低，終止飛行！")
        break

print(f"\n最終電量：{battery}%")
print("=" * 50)
