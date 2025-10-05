from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running! 🤖"

@app.route('/health')
def health():
    return {"status": "healthy", "bot": "telegram-bot"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
