import os
import requests

# Slack Webhook URLを環境変数から取得
slack_webhook_url = os.environ["SLACK_WEBHOOK_URL"]
message = {"text": "おはよう！GitHub Actionsからのメッセージだよ！"}

response = requests.post(slack_webhook_url, json=message)
print(response.text)