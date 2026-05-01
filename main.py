from playwright.sync_api import sync_playwright
import requests
import time

TOKEN = "8783362495:AAFNNvuZWysgDklNH9UiHK2nqJBzDG6B6P8"
CHAT_ID = "1202717318"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def check():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment")

        # نستنّاو الصفحة تكمل
        page.wait_for_timeout(8000)

        content = page.content()

        if "No appointments available" not in content:
            send("🚨🔥 موعد VFS إيطاليا متوفر! احجز بسرعة!")

        browser.close()

while True:
    try:
        check()
        time.sleep(60)
    except:
        time.sleep(120)
