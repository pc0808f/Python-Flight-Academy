"""
W4 範例 1：函數參數示範
學習重點：理解參數的作用
"""

# 無參數函數
def greet_fixed():
    print("你好，小明！")

# 有參數函數
def greet(name):
    print(f"你好，{name}！")

print("===== 無參數函數 =====")
greet_fixed()  # 只能打招呼給小明

print("\n===== 有參數函數 =====")
greet("小明")  # 可以對任何人打招呼
greet("小華")
greet("老師")

# 飛行函數範例
def fly(seconds):
    """模擬飛行指定秒數"""
    print(f"飛行 {seconds} 秒")

print("\n===== 飛行函數 =====")
fly(1)  # 飛 1 秒
fly(2)  # 飛 2 秒
fly(3)  # 飛 3 秒
