import requests
import time
import os

# ข้อมูล Bot จาก Environment
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ข้อความเตือนน้ำท่วม
ALERT_MSG = "🚨 แจ้งเตือนน้ำท่วม! กรุณาตรวจสอบพื้นที่ใกล้เคียงทันที"

# ตัวอย่างการดึงข้อมูลน้ำท่วม (ใส่ API จริงในภายหลัง)
def check_flood():
    return True  # ทดสอบให้แจ้งเตือนเสมอ

def send_alert():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": ALERT_MSG}
    requests.post(url, data=data)

if __name__ == "__main__":
    if check_flood():
        send_alert()
