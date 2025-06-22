from flask import Flask, Response
import requests

app = Flask(__name__)

# 取得したいURLをここで指定
TARGET_URL = 'https://noticeably-light-hen.ngrok-free.app/'

@app.route('/')
def fetch_html():

    try:
        headers = {
            'User-Agent': 'MyFlaskFetcher/1.0',  # 非標準なUA
            'Accept': 'text/html',
            'ngrok-skip-browser-warning': 'true' 
        }

        response = requests.get(TARGET_URL, headers=headers)        
        response.raise_for_status()
        # レスポンスのHTMLをそのまま返す
        return Response(response.text, mimetype='text/html')
    except requests.exceptions.RequestException as e:
        return f'Error fetching HTML: {e}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
