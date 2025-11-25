from playwright.sync_api import sync_playwright

def scrape_dynamic_page(url: str, wait_for_selector: str = "body") -> dict:
    
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=30000)

        page.wait_for_selector(wait_for_selector, timeout=10000)

        html = page.content()

        text = page.inner_text("body")

        browser.close()

    return {"html": html, "text": text}