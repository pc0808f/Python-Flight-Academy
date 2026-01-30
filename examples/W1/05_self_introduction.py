"""
W1 範例 5：自我介紹程式（綜合範例）
學習重點：整合所有 W1 學習內容
"""

# 個人資料
name = "王小明"
age = 16
school = "內湖高工"
grade = 1
height = 1.75  # 單位：公尺
weight = 65.0  # 單位：公斤

# 興趣愛好
hobby_1 = "打籃球"
hobby_2 = "寫程式"
hobby_3 = "玩無人機"

# 計算 BMI
bmi = weight / (height ** 2)

# 計算明年年齡
next_year_age = age + 1

# 輸出自我介紹
print("=" * 50)
print("　　　　　　自我介紹")
print("=" * 50)
print(f"姓名：{name}")
print(f"年齡：{age} 歲（明年 {next_year_age} 歲）")
print(f"學校：{school} {grade} 年級")
print(f"身高：{height} 公尺")
print(f"體重：{weight} 公斤")
print(f"BMI：{bmi:.2f}")
print("-" * 50)
print("我的興趣愛好：")
print(f"  1. {hobby_1}")
print(f"  2. {hobby_2}")
print(f"  3. {hobby_3}")
print("=" * 50)
print(f"我想學習用 Python 控制無人機！")
print("=" * 50)
