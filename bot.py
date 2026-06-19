import asyncio
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
import json

SESSION_FIL = "session.json"
BOKNINGS_URL = "https://fp.trafikverket.se/Boka/ng/"

with sync_playwright() as pw:
    browser = pw.firefox.launch(headless=False)
    context = browser.new_context()

    # Ladda sparad session
    cookies = json.loads(open(SESSION_FIL).read())
    context.add_cookies(cookies)
    print("Session laddad")

    page = context.new_page()
    page.goto(BOKNINGS_URL)
    page.wait_for_load_state("networkidle")

    print("URL:", page.url)
    print("Titel:", page.title())

    # Avgör om vi är inloggade eller omdirigerades till login
    if "login" in page.url.lower() or "logga-in" in page.url.lower():
        print("❌ Sessionen har gått ut – behöver logga in igen")
    else:
        print("✅ Sessionen fungerar – vi är inne!")

    input("Tryck Enter för att stänga...")
    browser.close()