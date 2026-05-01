import requests
import time
import random

TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

URL = "https://visa.vfsglobal.com/appointment/api/appointment/availability"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://visa.vfsglobal.com",
    "Referer": "https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment"
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

        print("Status:", r.status_code)

        # 🚫 إذا بلوك
        if r.status_code == 403:
            print("⛔ Blocked by VFS")
            return

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

                message = "🚨🔥 مواعيد ITALIE (Tourism)\n"
                message += "📍 Constantine / Annaba\n\n"
                message += "📅 التواريخ:\n"

                for d in dates_unique:
                    message += f"- {d}\n"

                send(message)

        else:
            print("Error status:", r.status_code)

    except Exception as e:
        print("Error:", e)

while True:
    check()

    # ⏱️ مهم: تأخير باش ما يتبلوكش
    time.sleep(random.randint(45, 90))
