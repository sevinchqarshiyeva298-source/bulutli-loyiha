import os
import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    muhit = os.environ.get("APP_ENV", "An'anaviy Lokal Muhit (Localhost)")
    server_vaqti = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({
        "holat": "Faol (Online)",
        "muhit": muhit,
        "server_vaqti": server_vaqti,
        "izoh": "Dastur muvaffaqiyatli ishga tushirildi!"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)