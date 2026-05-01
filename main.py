from playwright.sync_api import sync_playwright
import requests
import time

TOKEN = "8783362495:AAFNNvuZWysgDklNH9UiHK2nqJBzDG6B6P8"
CHAT_ID = "1202717318"

URL = "https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)

        # نستنى الموقع يحمل
        page.wait_for_timeout(10000)

        content = page.content().lower()

        # 🎯 فلترة مخصصة
        found_city = ("constantine" in content) or ("annaba" in content)
        found_tourism = ("tourism" in content) or ("touristique" in content)

        # ❗ إذا ما كاش "no appointments"
        available = "no appointments available" not in content

        if found_city and found_tourism and available:
            send("🚨🔥 موعد VFS ITALIE متوفر!\n📍 Constantine / Annaba\n🧳 Tourism\n🔥 احجز بسرعة!")

        browser.close()

while True:
    try:
        check()
        time.sleep(60)
    except:
        time.sleep(120)
