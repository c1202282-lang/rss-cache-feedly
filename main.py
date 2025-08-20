import requests
from datetime import datetime

# لینک RSS اصلی
SOURCE_URL = "https://rss.app/feeds/CtWXgEfkS4cW7kJ9.xml"
OUTPUT_FILE = "feed.xml"

def fetch_and_save_rss():
    print(f"[{datetime.utcnow()}] Fetching RSS from {SOURCE_URL}")
    try:
        r = requests.get(SOURCE_URL, timeout=20)
        r.raise_for_status()

        # ذخیره محتوا
        with open(OUTPUT_FILE, "wb") as f:
            f.write(r.content)

        print(f"[{datetime.utcnow()}] RSS saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error fetching RSS: {e}")

if __name__ == "__main__":
    fetch_and_save_rss()
