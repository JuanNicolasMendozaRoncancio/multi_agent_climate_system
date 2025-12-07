from playwright.sync_api import sync_playwright
from src.utils.paywall_detector import detect_paywall

def scrape_dynamic_page(url: str, wait_for_selector: str = "body") -> dict:
    
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_selector(wait_for_selector, timeout=10000)

        html = page.content()
        title = page.title()
        text = page.inner_text("body")

        browser.close()
        
        # if detect_paywall(html):
        #     return None

    return {"title": title,"html": html, "text": text}