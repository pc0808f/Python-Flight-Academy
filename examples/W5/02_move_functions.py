"""
W5 範例 2：移動函數設計
學習重點：設計前後左右移動函數
"""

import time

def move_forward(distance):
    """向前移動"""
    print(f"➡️  向前移動 {distance} 單位")
    time.sleep(distance)

def move_backward(distance):
    """向後移動"""
    print(f"⬅️  向後移動 {distance} 單位")
    time.sleep(distance)

def move_left(distance):
    """向左移動"""
    print(f"⬆️  向左移動 {distance} 單位")
    time.sleep(distance)

def move_right(distance):
    """向右移動"""
    print(f"⬇️  向右移動 {distance} 單位")
    time.sleep(distance)

print("===== 移動函數示範 =====\n")

# 測試移動函數
print("1. 向前移動")
move_forward(1)

print("\n2. 向右移動")
move_right(1)

print("\n3. 向後移動")
move_backward(1)

print("\n4. 向左移動")
move_left(1)

print("\n✅ 回到原點")
