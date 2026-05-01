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
    print("📤 Sending:", msg)
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    print("🔍 Checking VFS...")

    try:
        r = requests.post(URL, json=payload, headers=headers, timeout=20)

        print("Status:", r.status_code)

        data = r.text.lower()

        # 🧪 وضع الاختبار (مفعل)
        if True:
            send("🧪 TEST: البوت يخدم ويفحص كل دقيقة ✅")

        # 🔥 الوضع الحقيقي (رجعو بعد الاختبار)
        # if ("constantine" in data or "annaba" in data) and ("available" in data):
        #     send("🚨 موعد ITALIE Tourism متوفر في Constantine / Annaba 🔥")

    except Exception as e:
        print("❌ Error:", e)

while True:
    check()
    time.sleep(random.randint(30, 60))
