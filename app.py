from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Telegram Bot Token và Chat ID
TELEGRAM_BOT_TOKEN = "6307584784:AAEMKGGVtUlx-oOWRCIuCqghp8tqO-oUkzI"  # Thay bằng token của bạn
TELEGRAM_CHAT_ID = "-4191688148"  # Thay bằng chat ID

# Hàm gửi tin nhắn đến Telegram
def send_to_telegram(data):
    name = data.get("name", "Không có tên")
    email = data.get("email", "Không có email")

    message = f"📨 *Dữ Liệu Mới Nhận Được:*\n- Họ và Tên: {name}\n- Email: {email}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

# Route nhận dữ liệu từ Form
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        send_to_telegram(data)
        return jsonify({"status": "success", "message": "Dữ liệu đã được gửi đến Telegram"}), 200
    return jsonify({"status": "error", "message": "Không có dữ liệu"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
