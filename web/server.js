const express = require('express');
const cors = require('cors');
const axios = require('axios');
const app = express();
const port = 3000;

// 設定請求超時（毫秒）
const REQUEST_TIMEOUT = 10000;

// 啟用 CORS
app.use(cors());

// 提供靜態檔案
app.use(express.static('.'));

// 代理端點
app.get('/proxy/vd', async (req, res) => {
    try {
        const response = await axios.get('https://tisvcloud.freeway.gov.tw/history/motc20/VDLive.xml', {
            timeout: REQUEST_TIMEOUT,
            validateStatus: function (status) {
                return status >= 200 && status < 500; // 接受所有非 500 錯誤的狀態碼
            }
        });
        
        // 檢查回應內容
        if (!response.data || response.data.length === 0) {
            throw new Error('回應內容為空');
        }
        
        res.set('Content-Type', 'application/xml');
        res.send(response.data);
    } catch (error) {
        console.error('代理請求失敗:', error);
        
        if (error.code === 'ECONNABORTED') {
            res.status(504).send('請求超時，請稍後再試');
        } else if (error.response) {
            // 伺服器回應了錯誤狀態碼
            res.status(error.response.status).send(`伺服器錯誤：${error.response.status}`);
        } else if (error.request) {
            // 請求已發送但沒有收到回應
            res.status(503).send('無法連接到伺服器');
        } else {
            // 請求設定時發生錯誤
            res.status(500).send('代理請求失敗');
        }
    }
});

app.listen(port, () => {
    console.log(`伺服器運行在 http://localhost:${port}`);
}); 