# 本地開發環境設定

本資料夾包含了兩種版本的本地代理伺服器，您可以選擇使用 Python 或 Node.js 版本。

## Python 版本

### 前置需求
- Python 3.x
- pip（Python 套件管理器）

### 安裝步驟
1. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 啟動代理伺服器：
   ```bash
   python proxy_server.py
   ```

3. 在瀏覽器中開啟：
   - 本機：http://localhost:5000
   - 手機：http://[本機IP]:5000

## Node.js 版本

### 前置需求
- Node.js
- npm（Node.js 套件管理器）

### 安裝步驟
1. 安裝相依套件：
   ```bash
   npm install
   ```

2. 啟動代理伺服器：
   ```bash
   npm start
   ```

3. 在瀏覽器中開啟：
   - 本機：http://localhost:3000
   - 手機：http://[本機IP]:3000

## 功能說明

- 代理伺服器會自動處理 CORS 問題
- 支援 XML 資料的解壓縮
- 包含完整的錯誤處理和日誌記錄
- 請求超時設定為 10 秒

## 注意事項

1. 確保您的網路可以連接到目標伺服器
2. 如果遇到連線問題，請檢查防火牆設定
3. 手機連線時，請確保手機和電腦在同一個網路中

## 錯誤排除

### Python 版本
- 如果出現 `ModuleNotFoundError`，請確認已安裝所有相依套件
- 如果出現 `Address already in use`，請確認沒有其他程式使用 5000 端口

### Node.js 版本
- 如果出現 `EADDRINUSE`，請確認沒有其他程式使用 3000 端口
- 如果出現 `Cannot find module`，請確認已安裝所有相依套件 