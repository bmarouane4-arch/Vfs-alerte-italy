import requests
import time
import random

TOKEN = "8783362495:AAFNNvuZWysgDklNH9UiHK2nqJBzDG6B6P8"
CHAT_ID = "1202717318"

URL = "https://visa.vfsglobal.com/appointment/api/appointment/availability"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

payload = {
    "countryCode": "dza",
    "missionCode": "ita",
    "centerCode": "",
    "categoryCode": "tourism"
}

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    try:
        r = requests.post(URL, json=payload, headers=headers, timeout=20)

        if r.status_code == 200:
            data = r.text.lower()

            # 🎯 فلترة:
            has_city = ("constantine" in data) or ("annaba" in data)
            has_available = ("available" in data)

            if has_city and has_available:
                send("🚨🔥 موعد ITALIE (Tourism) متوفر!\n📍 Constantine / Annaba\n⚡ احجز بسرعة!")

        else:
            print("Status error:", r.status_code)

    except Exception as e:
        print("Error:", e)

while True:
    check()
    time.sleep(random.randint(30, 60))
