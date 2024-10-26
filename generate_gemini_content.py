import requests
import json

# Gemini API エンドポイントとキーの設定
API_URL = "https://api.gemini.com/generate"
API_KEY = "your_gemini_api_key"

# プロンプトをファイルから読み込み
with open('prompt.json', 'r') as f:
    data = json.load(f)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# Gemini API から生成されたコンテンツを取得
response = requests.post(API_URL, json=data, headers=headers)

if response.status_code == 200:
    content = response.json().get("text")
    with open("generated_content.txt", "w") as f:
        f.write(content)
else:
    raise Exception(f"Error generating content: {response.status_code}, {response.text}")
