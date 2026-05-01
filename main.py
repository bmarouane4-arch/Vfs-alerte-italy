import requests
import time
import random

TOKEN = "8783362495:AAFNNvuZWysgDklNH9UiHK2nqJBzDG6B6P8"
CHAT_ID = "1202717318"

URL = "https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check_vfs():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    r = requests.get(URL, headers=headers)

    # ⚠️ هذا الشرط ممكن ما يكونش دقيق بسبب JavaScript
    if "No appointments available" not in r.text:
        send("🚨 موعد VFS إيطاليا متوفر! احجز بسرعة!")

while True:
    try:
        check_vfs()
        time.sleep(random.randint(30, 60))
    except:
        time.sleep(60)
