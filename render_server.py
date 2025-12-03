import threading
from flask import Flask
import asyncio
import main

app = Flask(__name__)

@app.route("/")
def home():
    return "Extractor Bot is running on Render!"

def start_bot():
    asyncio.run(main.start_bot())

threading.Thread(target=start_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
