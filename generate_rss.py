import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime

URL = "https://www.c14.co.il/"

html = requests.get(URL, timeout=15).text
soup = BeautifulSoup(html, "html.parser")

fg = FeedGenerator()
fg.title("C14 News")
fg.link(href=URL)
fg.description("עדכוני חדשות מאתר C14")

links = soup.select("a")

for a in links:
    title = a.get_text(strip=True)
    link = a.get("href")

    if not title or not link or len(title) < 10:
        continue

    if link.startswith("/"):
        link = URL.rstrip("/") + link

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=link)
    fe.published(datetime.utcnow())

fg.rss_file("rss.xml")

