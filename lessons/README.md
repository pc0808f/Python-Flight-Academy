# 教案資料夾

本資料夾包含「飛行驅動 Python」課程的詳細教案與範例程式碼。

---

## 📂 資料夾結構

```
lessons/
├── W1/                 # 第一週：Python 環境建置與基礎語法
│   └── W1_教案.md
├── W2/                 # 第二週：Webots 模擬器環境設置
│   └── W2_教案.md
├── W3/                 # 第三週：模擬器中的起飛與降落
│   └── W3_教案.md
└── README.md          # 本文件

examples/
├── W1/                 # W1 範例程式碼
│   ├── 01_hello.py
│   ├── 02_variables.py
│   ├── 03_fstring.py
│   ├── 04_calculation.py
│   └── 05_self_introduction.py
├── W2/                 # W2 範例程式碼
│   ├── 01_basic_robot.py
│   ├── 02_step_counter.py
│   ├── 03_motor_activation.py
│   └── 04_startup_screen.py
└── W3/                 # W3 範例程式碼
    ├── 01_wrong_no_sleep.py
    ├── 02_basic_takeoff_land.py
    ├── 03_multiple_takeoffs.py
    ├── 04_stair_climb.py
    └── 05_smooth_landing.py
```

---

## 📖 各週教案內容

### W1：Python 環境建置與基礎語法

**教學目標**
- 完成 Python 開發環境安裝
- 理解變數、資料型態的基本概念
- 學習使用 print() 和 f-string

**範例程式**
- `01_hello.py` - Hello Python 基礎輸出
- `02_variables.py` - 變數與資料型態
- `03_fstring.py` - 字串格式化
- `04_calculation.py` - 算術運算
- `05_self_introduction.py` - 綜合範例：自我介紹

**作業**
1. 自我介紹程式（必做）
2. 創意計算機（選做）

---

### W2：Webots 模擬器環境設置

**教學目標**
- 安裝並設定 Webots 模擬器
- 認識物件導向程式設計基本概念
- 理解 import 指令的作用
- 第一個無人機控制程式

**範例程式**
- `01_basic_robot.py` - 基本 Robot 物件
- `02_step_counter.py` - 步數計數器
- `03_motor_activation.py` - 啟動馬達
- `04_startup_screen.py` - 創意啟動畫面

**作業**
1. 環境檢核（必做）
2. 物件練習（必做）
3. 創意輸出（選做）

---

### W3：模擬器中的起飛與降落

**教學目標**
- 理解程式執行的順序性
- 認識 time.sleep() 函數的作用
- 控制虛擬無人機起飛與降落
- 調整參數控制飛行

**範例程式**
- `01_wrong_no_sleep.py` - 錯誤範例：沒有 sleep
- `02_basic_takeoff_land.py` - 基礎起飛與降落
- `03_multiple_takeoffs.py` - 連續起降
- `04_stair_climb.py` - 階梯式上升
- `05_smooth_landing.py` - 平穩降落

**作業**
1. 標準起降（必做）
2. 連續起降（必做）
3. 創意飛行（選做）

---

## 🎯 教案使用指南

### 給授課教師

#### 課前準備
1. 閱讀完整教案（150 分鐘課程）
2. 測試所有範例程式碼
3. 準備教學簡報（PPT）
4. 確認軟體環境已安裝

#### 教學建議
- **時間分配**：每節課 50 分鐘，建議嚴格控制
- **實作比重**：理論 30% + 實作 70%
- **巡視協助**：實作時間教師巡視，及時協助
- **差異化教學**：提供基礎版與進階版任務

#### 評量方式
- **形成性評量**：課堂觀察、實作練習
- **總結性評量**：每週作業（評分標準見教案）

---

### 給學生

#### 學習建議
1. **課前預習**：閱讀下週教案，了解學習目標
2. **上課專注**：實作時間動手練習，不只看老師操作
3. **課後複習**：重新執行範例程式，理解每一行代碼
4. **完成作業**：作業是檢驗學習成果的最佳方式

#### 自主學習
- 所有範例程式碼都可以在 `examples/` 資料夾找到
- 鼓勵修改參數、實驗不同效果
- 遇到問題先查看教案的「常見問題」章節
- 可以參考補充資源自學延伸

---

## 💻 範例程式碼使用方式

### 執行 W1 範例（Python）

```bash
# 進入 examples/W1 資料夾
cd examples/W1

# 執行範例程式
python 01_hello.py
python 02_variables.py
# ... 依此類推
```

### 執行 W2-W3 範例（Webots）

1. 開啟 Webots 模擬器
2. 載入 Crazyflie 世界（`File` > `Open World` > `crazyflie.wbt`）
3. 在場景樹中選擇 Crazyflie
4. 將控制器程式替換為範例程式碼
5. 點擊 ▶️ Play 執行

---

## 📊 學習進度追蹤

建議教師使用以下表格追蹤學生學習進度：

| 學號 | 姓名 | W1 作業 | W2 作業 | W3 作業 | 備註 |
|-----|------|--------|--------|--------|------|
|     |      | ☐      | ☐      | ☐      |      |

---

## 🔄 教案更新記錄

| 版本 | 日期 | 更新內容 |
|-----|------|---------|
| v1.0 | 2026-01-30 | 初版發布（W1-W3 教案） |

---

## 📞 問題回報

如果發現教案中有錯誤或建議改進，請透過以下方式回報：

- **GitHub Issues**：https://github.com/pc0808f/Python-Flight-Academy/issues
- **Email**：（待填寫）

---

## 📄 授權資訊

本教案採用 [MIT License](../LICENSE) 授權，歡迎自由使用與修改。

---

**編撰團隊**：Python Flight Academy
**最後更新**：2026-01-30
