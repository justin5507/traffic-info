const express = require('express');
const cors = require('cors');
const axios = require('axios');
const app = express();
const port = 3000;

// 啟用 CORS
app.use(cors());

// 提供靜態檔案
app.use(express.static('.'));

// 代理端點
app.get('/proxy/vd', async (req, res) => {
    try {
        const response = await axios.get('https://tisvcloud.freeway.gov.tw/history/motc20/VDLive.xml');
        res.set('Content-Type', 'application/xml');
        res.send(response.data);
    } catch (error) {
        console.error('代理請求失敗:', error);
        res.status(500).send('代理請求失敗');
    }
});

app.listen(port, () => {
    console.log(`伺服器運行在 http://localhost:${port}`);
}); 