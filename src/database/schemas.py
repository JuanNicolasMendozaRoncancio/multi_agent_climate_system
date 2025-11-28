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