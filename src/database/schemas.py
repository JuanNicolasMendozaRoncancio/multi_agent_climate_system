from datetime import datetime, timezone
from typing import Optional, Dict

def raw_document(source, url, text, html: Optional[str] = None, metadata: Optional[Dict] = None) -> Dict:
    return {
        "_type": "raw",
        "source": source,
        "url": url,
        "text": text,
        "html": html,
        "metadata": metadata or {},
        "timestamp": datetime.now(timezone.utc),
    }