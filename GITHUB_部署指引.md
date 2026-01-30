# GitHub 部署指引

本文件說明如何將專案上傳到 GitHub 並啟用 GitHub Pages。

---

## 📋 前置作業

已完成的項目：
- ✅ Git 儲存庫已初始化
- ✅ 所有文件已提交到本地儲存庫
- ✅ GitHub Pages 網站文件已建立（docs/ 目錄）

---

## 🚀 步驟一：在 GitHub 建立遠端儲存庫

### 1. 登入 GitHub
前往 https://github.com 並登入你的帳號

### 2. 建立新的儲存庫
1. 點擊右上角的 `+` 號
2. 選擇 `New repository`
3. 填寫以下資訊：
   - **Repository name**：`Python-Flight-Academy`
   - **Description**：`飛行驅動 Python - 18週高中無人機程式設計實作課程`
   - **Public** / Private：選擇 `Public`（公開）
   - **❌ 不要** 勾選 "Initialize this repository with a README"（因為我們已經有了）
4. 點擊 `Create repository`

---

## 📤 步驟二：推送到 GitHub

### 在命令列執行以下指令：

```bash
# 1. 設定遠端儲存庫（請將 YOUR_USERNAME 替換成你的 GitHub 使用者名稱）
git remote add origin https://github.com/YOUR_USERNAME/Python-Flight-Academy.git

# 2. 確認遠端儲存庫已設定
git remote -v

# 3. 推送到 GitHub（首次推送）
git push -u origin master
```

### 推送完成後
前往你的 GitHub 儲存庫頁面（https://github.com/YOUR_USERNAME/Python-Flight-Academy），應該可以看到所有文件已經上傳成功！

---

## 🌐 步驟三：啟用 GitHub Pages

### 1. 進入 Settings
在你的儲存庫頁面，點擊 `Settings`（設定）

### 2. 找到 Pages 設定
在左側選單中找到並點擊 `Pages`

### 3. 配置 GitHub Pages
在 "Build and deployment" 區域：
- **Source**：選擇 `Deploy from a branch`
- **Branch**：選擇 `master` 分支
- **Folder**：選擇 `/docs`
- 點擊 `Save`（儲存）

### 4. 等待部署
- GitHub 會開始建置你的網站
- 大約 1-2 分鐘後，頁面上方會顯示網站網址
- 網址格式：`https://YOUR_USERNAME.github.io/Python-Flight-Academy/`

---

## ✅ 步驟四：驗證部署成功

### 檢查網站
1. 點擊 GitHub Pages 提供的網址
2. 應該可以看到課程展示網站
3. 測試導航連結是否正常運作

### 如果遇到問題
- 確認 `docs/index.html` 檔案存在
- 確認 GitHub Pages 設定的資料夾為 `/docs`
- 等待幾分鐘後重新整理頁面

---

## 🔗 步驟五：更新文件中的連結

### 需要更新的文件：

#### 1. README.md
找到並替換以下內容：
```markdown
# 將所有 "你的帳號" 替換成實際的 GitHub 使用者名稱
https://github.com/你的帳號/Python-Flight-Academy
```

#### 2. docs/index.html
找到並替換以下內容：
```html
<!-- 搜尋 "你的帳號" 並替換成實際的 GitHub 使用者名稱 -->
https://github.com/你的帳號/Python-Flight-Academy
```

### 更新後重新提交：

```bash
# 1. 修改文件後，加入變更
git add README.md docs/index.html

# 2. 提交變更
git commit -m "Update GitHub repository links"

# 3. 推送到 GitHub
git push
```

---

## 📊 步驟六：分享給合作教師

### GitHub Pages 網址
部署完成後，你可以將以下網址分享給合作的老師：

```
https://YOUR_USERNAME.github.io/Python-Flight-Academy/
```

### 網站特色
✨ **互動式展示頁面**：
- 課程簡介與目標
- 18 週完整進度表
- 三階段學習模式說明
- 課程特色與優勢
- 所需設備清單
- 教學資源連結

✨ **完整課程文件**：
- [課程規劃表](課程規劃表_v1.0.md)
- [週次進度表](週次進度表.md)
- [課程大綱詳細版](課程大綱_詳細版.md)

---

## 🛠️ 後續維護

### 更新課程內容
當需要更新課程內容時：

```bash
# 1. 修改文件
# 2. 提交變更
git add .
git commit -m "更新課程內容：說明變更內容"

# 3. 推送到 GitHub
git push

# 4. GitHub Pages 會自動重新部署（約 1-2 分鐘）
```

### 查看部署狀態
在 GitHub 儲存庫頁面：
1. 點擊 `Actions` 標籤
2. 可以看到 GitHub Pages 的部署狀態

---

## 📧 分享範例訊息

你可以使用以下範例訊息邀請老師查看課程：

```
親愛的 XX 老師您好：

我完成了「飛行驅動 Python」18 週無人機程式設計課程的規劃，
這是一個結合 Crazyflie 無人機與 Python 程式設計的高中課程。

📚 課程網站：https://YOUR_USERNAME.github.io/Python-Flight-Academy/
💻 GitHub 專案：https://github.com/YOUR_USERNAME/Python-Flight-Academy

課程特色：
✅ 三階段學習模式（模擬器 → 實機組裝 → 程式飛行）
✅ 符合 108 課綱資訊科技素養指標
✅ 完整的 18 週教學規劃與評量設計
✅ 詳細的設備清單與預算估算

歡迎查看並提供寶貴意見，期待與您合作！

敬祝
教安

XXX 敬上
```

---

## ❓ 常見問題

### Q1: GitHub Pages 顯示 404 錯誤
**A:**
- 確認 Settings > Pages 中的資料夾設定為 `/docs`
- 確認 `docs/index.html` 檔案存在
- 等待 1-2 分鐘讓 GitHub 完成部署

### Q2: 網站樣式沒有載入
**A:**
- 檢查 `docs/style.css` 檔案是否存在
- 清除瀏覽器快取後重新整理

### Q3: 如何讓網站使用自訂網域？
**A:**
- 在 Settings > Pages 中可以設定 Custom domain
- 需要在你的網域提供商設定 DNS 記錄

### Q4: 可以設為私人儲存庫嗎？
**A:**
- 可以，但 GitHub Pages 在私人儲存庫需要 GitHub Pro 方案
- 建議使用公開儲存庫以便教師查看

---

## 🎉 完成！

恭喜你完成 GitHub 部署！

現在你可以：
- ✅ 分享課程網站給合作教師
- ✅ 隨時更新課程內容
- ✅ 接收他人的建議與回饋（透過 GitHub Issues）
- ✅ 讓其他教師 fork 你的專案

---

**製作日期**：2026-01-30
**版本**：v1.0
