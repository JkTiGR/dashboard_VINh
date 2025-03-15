from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "8099553216:AAEE3Ctou3yY4ddwVbXiUfHgfT7PeZyUyhA"
CHAT_ID = "-1002239976197"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({"error": "Message is required"}), 400

        response = requests.post(TELEGRAM_URL, json={"chat_id": CHAT_ID, "text": message})

        if response.status_code == 200:
            return jsonify({"success": True})
        else:
            return jsonify({"error": "Failed to send message", "details": response.text}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)