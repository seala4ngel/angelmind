import requests

class Notifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_slack(self, message):
        requests.post(self.webhook_url, json={"text": message})

    def send_telegram(self, bot_token, chat_id, message):
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, json={"chat_id": chat_id, "text": message})
