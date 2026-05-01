import requests
import time
import random

TOKEN = "YOUR_TOKEN"
CHAT_ID = "1202717318"  # 👈 أنت فقط

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
            data = r.json()

            dates_found = []

            if isinstance(data, list):
                for item in data:
                    text = str(item).lower()

                    if ("constantine" in text or "annaba" in text) and ("available" in text):
                        date = (
                            item.get("date") or
                            item.get("appointmentDate") or
                            item.get("slotDate")
                        )
                        if date:
                            dates_found.append(date)

            if dates_found:
                dates_unique = sorted(set(dates_found))

                message = "🚨🔥 مواعيد ITALIE (Tourism) متوفرة!\n"
                message += "📍 Constantine / Annaba\n\n"
                message += "📅 التواريخ:\n"

                for d in dates_unique:
                    message += f"- {d}\n"

                send(message)

        else:
            print("Status error:", r.status_code)

    except Exception as e:
        print("Error:", e)

while True:
    check()
    time.sleep(random.randint(30, 60))
