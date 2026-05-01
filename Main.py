8783362495import requests
import time
import random

TOKEN = "8783362495:AAFNNvuZWysgDklNH9UiHK2nqJBzDG6B6P8"
CHAT_ID = "918455655"

URL = "https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_vfs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers)

    # إذا لقى موعد
    if "No appointments available" not in r.text:
        send_telegram("🚨 يوجد موعد VFS إيطاليا متوفر! احجز بسرعة!")

while True:
    try:
        check_vfs()
        time.sleep(random.randint(30, 60))
    except:
        time.sleep(60)
