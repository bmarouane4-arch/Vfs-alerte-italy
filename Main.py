import requests
import time
import os

TOKEN = os.getenv("8783362495:AAHqDon_R9bg5MEYW7yaFN3hyesn9sLi9Qw")
CHAT_ID = os.getenv("1777639751")

URL = "https://visa.vfsglobal.com/dza/fr/ita/book-an-appointment"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_vfs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers)

    if True:
        send_telegram("🚨 RDV Italie disponible (Constantine / Annaba) !")

while True:
    try:
        check_vfs()
        time.sleep(60)  # كل دقيقة
    except:
        time.sleep(120)
