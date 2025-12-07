from bs4 import BeautifulSoup

PAYWALL_KEYWORDS = [
    "paywall", "metered", "subscribe", "premium", 
    "login required", "subscriber", "restricted"
]

PAYWALL_SELECTORS = [
    ".paywall", "#paywall", ".subscription", ".premium",
    "div[class*='meter']", "div[data-test*='paywall']"
]

def detect_paywall(html: str) -> bool:
    """
    Detecta si una página tiene un paywall.
    Retorna True si se detecta paywall.
    """
    soup = BeautifulSoup(html, "html.parser")
    
    # 1. palabras clave
    text = soup.get_text().lower()
    if any(kw in text for kw in PAYWALL_KEYWORDS):
        return True
    
    # 2. selectores típicos
    for selector in PAYWALL_SELECTORS:
        if soup.select_one(selector):
            return True
    
    return False
