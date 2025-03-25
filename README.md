# 即時路況資訊系統

🌐 **[立即前往網頁](https://justin5507.github.io/traffic-info/)**

這是一個即時路況資訊系統，可以顯示台灣高速公路的即時交通資訊，包括車速、車流量和設備狀態等數據。

## 功能特色

- 🔄 自動每分鐘更新資料
- 📊 多種篩選功能：
  - 車道類型篩選
  - 設備狀態篩選
  - 速率範圍篩選
  - 設備代碼/路段代碼搜尋
- 📋 資料排序功能
- 📥 資料匯出成 Excel（CSV）格式
- 📱 支援手機版面配置

## 使用說明

### 基本操作

1. **查看資料**
   - 進入網頁後會自動載入最新資料
   - 資料每分鐘自動更新一次
   - 可點擊「更新資料」按鈕手動更新

2. **篩選資料**
   - 使用上方的下拉選單選擇車道類型
   - 使用狀態選單篩選設備狀態
   - 輸入速率範圍進行篩選
   - 在搜尋框輸入設備代碼或路段代碼

3. **排序功能**
   - 點擊表格標題列可依該欄位排序
   - 再次點擊可切換升序/降序

4. **匯出資料**
   - 點擊「匯出 Excel」按鈕
   - 系統會自動下載當前篩選結果的 CSV 檔案

### 開發說明

本專案包含兩種執行方式：

1. **直接使用網頁版**
   - 透過 GitHub Pages 部署
   - 使用公開 CORS 代理服務
   - 無需安裝任何軟體

2. **本地開發版本**
   - 需要安裝 Python 或 Node.js
   - 提供本地代理伺服器避免 CORS 問題

#### Python 版本安裝步驟

1. 安裝 Python 3.x
2. 安裝相依套件：
   ```bash
   cd web
   pip install -r requirements.txt
   ```
3. 執行代理伺服器：
   ```bash
   python proxy_server.py
   ```
4. 開啟 `web/index.html`

#### Node.js 版本安裝步驟

1. 安裝 Node.js
2. 安裝相依套件：
   ```bash
   cd web
   npm install
   ```
3. 執行代理伺服器：
   ```bash
   node server.js
   ```
4. 開啟 `web/index.html`

## 檔案結構

```
traffic-info/
├── README.md           # 專案說明文件
├── index.html          # 主要網頁檔案
├── web/               # 開發相關檔案
│   ├── proxy_server.py  # Python 版代理伺服器
│   ├── requirements.txt # Python 相依套件
│   ├── server.js       # Node.js 版代理伺服器
│   └── package.json    # Node.js 相依套件
└── ref/               # 參考文件
```

## 資料來源

資料來自交通部高速公路局的開放資料 API：
- 即時路況資訊：https://tisvcloud.freeway.gov.tw/history/motc20/VDLive.xml

## 授權資訊

本專案採用 MIT 授權條款。 