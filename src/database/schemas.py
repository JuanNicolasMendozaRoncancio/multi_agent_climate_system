from datetime import datetime, timezone
from typing import Optional, Dict
from pydantic import BaseModel, Field

class RawDocument(BaseModel):
    source: str = Field(..., description="Source of the document")
    title: Optional[str] = None
    content: str = Field(..., description="Content of the document")
    url: Optional[str] = None
    published_at: Optional[datetime] = None
    raw_metadata: Dict = Field(default_factory=dict)
    inserted_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    def to_mongo(self) -> Dict:
        return {
            "_type": "raw",
            "source": self.source,
            "title": self.title,
            "content": self.content,
            "url": self.url,
            "published_at": self.published_at,
            "raw_metadata": self.raw_metadata,
            "inserted_at": self.inserted_at,
        }
    
def raw_article_schema(url, text, html, title, source, scraper_used, parent_id=None, published_at=None):
    return {
        "_type": "raw",
        "source": source,
        "url": url,
        "text": text,
        "html": html,
        "title": title,
        "published_at": published_at,
        "scraper_used": scraper_used,
        "raw_metadata": {
            "processed_at": datetime.now(timezone.utc),
            "parent_id": parent_id,
            "status": "new"
        }
    }