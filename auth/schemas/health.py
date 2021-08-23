from typing import Optional
from uuid import UUID


class Health:
    owner_id: UUID
    title: str
    value: Optional[float]
    measure: Optional[str]
