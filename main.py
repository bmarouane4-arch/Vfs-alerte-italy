import requests
import time
import random

TOKEN = "YOUR_TOKEN"

# 🔐 الكود السري
ACCESS_CODE = "1234"

# 👥 المستخدمين المسموحين
ALLOWED_USERS = ["1202717318"]

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

# 📩 إرسال
def send(msg, chat_id):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": chat_id, "text": msg}
    )

# 🧠 استقبال الرسائل
def check_messages():
    global ALLOWED_USERS

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url).json()

    for update in r.get("result", []):
        message = update.get("message", {})
        chat_id = str(message.get("chat", {}).get("id"))
        text = message.get("text", "")

        if text == "/start":
            send("🔐 أرسل الكود للدخول", chat_id)

        elif text == ACCESS_CODE:
            if chat_id not in ALLOWED_USERS:
                ALLOWED_USERS.append(chat_id)
                send("✅ تم التفعيل! ستصلك المواعيد", chat_id)

        else:
            send("❌ كود خاطئ", chat_id)

# 📢 إرسال للجميع
def broadcast(msg):
    for user in ALLOWED_USERS:
        send(msg, user)

# 🔍 فحص VFS
def check_vfs():
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

                message = "🚨🔥 مواعيد متوفرة!\n📍 Constantine / Annaba\n\n📅:\n"
                for d in dates_unique:
                    message += f"- {d}\n"

                broadcast(message)

    except Exception as e:
        print(e)

# 🔁 التشغيل
while True:
    check_messages()
    check_vfs()
    time.sleep(random.randint(30, 60))
