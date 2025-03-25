from flask import Flask, Response
from flask_cors import CORS
import requests
import logging
import gzip
import io
import socket

# 設定日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# 設定請求超時（秒）
REQUEST_TIMEOUT = 10

def get_local_ip():
    try:
        # 獲取本機 IP 地址
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

@app.route('/proxy/vd')
def proxy_vd():
    try:
        url = 'https://tisvcloud.freeway.gov.tw/history/motc20/VDLive.xml'
        logger.info(f'正在請求：{url}')
        
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        logger.info(f'回應狀態碼：{response.status_code}')
        logger.info(f'回應標頭：{response.headers}')
        
        if response.status_code != 200:
            logger.error(f'請求失敗：{response.status_code} - {response.text}')
            return f'請求失敗：{response.status_code}', response.status_code
            
        # 檢查內容是否為 XML
        content = response.content
        if content.startswith(b'<?xml'):
            logger.info('內容已經是 XML 格式')
        else:
            # 嘗試解壓縮
            try:
                logger.info('嘗試解壓縮內容')
                content = gzip.GzipFile(fileobj=io.BytesIO(content)).read()
                logger.info('成功解壓縮')
            except Exception as e:
                logger.warning(f'解壓縮失敗，使用原始內容：{str(e)}')
            
        logger.info(f'處理後資料長度：{len(content)} 位元組')
        logger.info(f'資料前 100 字元：{content[:100]}')
        
        if len(content) == 0:
            logger.error('處理後的資料為空')
            return '處理後的資料為空', 500
            
        return Response(content, content_type='application/xml')
    except requests.exceptions.Timeout:
        logger.error('請求超時')
        return '請求超時，請稍後再試', 504
    except requests.exceptions.RequestException as e:
        logger.error(f'請求異常：{str(e)}')
        return f'請求異常：{str(e)}', 500
    except Exception as e:
        logger.error(f'未知錯誤：{str(e)}')
        return f'未知錯誤：{str(e)}', 500

if __name__ == '__main__':
    local_ip = get_local_ip()
    logger.info(f'本機 IP 地址：{local_ip}')
    logger.info(f'請在手機瀏覽器中輸入：http://{local_ip}:5000')
    logger.info('啟動代理伺服器...')
    app.run(port=5000, debug=True) 