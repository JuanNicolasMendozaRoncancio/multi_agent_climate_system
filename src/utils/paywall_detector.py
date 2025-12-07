from bs4 import BeautifulSoup

PAYWALL_KEYWORDS = [
    "paywall", "metered", "subscribe to read", 
    "please subscribe", "subscription required"
]

# selectores mucho más específicos
PAYWALL_SELECTORS = [
    ".paywall", 
    "div.paywall",
    "div[data-component='paywall']",
    "div[id*='paywall']",
    "div[class*='paywall']",
    "div[class*='subscription-required']"
]


def detect_paywall(html: str) -> bool:
    """
    Detector RELAJADO de paywall.
    Solo activa si se detecta fuerte evidencia.
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True).lower()
    text_length = len(text)

    if text_length < 300:
        low_text = True
    else:
        low_text = False

    keyword_hit = any(kw in text for kw in PAYWALL_KEYWORDS)

    selector_hit = any(soup.select(selector) for selector in PAYWALL_SELECTORS)

    if (keyword_hit and low_text) or selector_hit:
        return True

    return False
