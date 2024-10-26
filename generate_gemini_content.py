import requests
import json

# 正しいエンドポイントとAPIキーを設定
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
API_KEY = "AIzaSyCE9pYu_m3516CimJvdi_5T3PP2re6InrM"  # あなたのAPIキーを入力してください

# プロンプトをファイルから読み込み
with open('prompt.json', 'r') as f:
    data = json.load(f)

# APIキーをURLに追加
full_url = f"{API_URL}?key={API_KEY}"

headers = {
    "Content-Type": "application/json",
}

# Gemini API から生成されたコンテンツを取得
response = requests.post(full_url, json=data, headers=headers)

# デバッグ用: レスポンスの内容を表示
print("Response Status Code:", response.status_code)
print("Response Text:", response.text)

# レスポンスが正常かどうか確認
if response.status_code == 200:
    try:
        # 修正: candidatesからコンテンツを取得
        content = response.json().get("candidates")[0].get("content").get("parts")[0].get("text")
        with open("generated_content.txt", "w") as f:
            f.write(content)
    except (IndexError, TypeError) as e:
        raise Exception(f"Unexpected response structure: {response.json()}")
else:
    raise Exception(f"Error generating content: {response.status_code}, {response.text}")
