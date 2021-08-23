from datetime import datetime
from typing import Optional
from uuid import UUID


class Subscription:
    owner_id: UUID
    type_subscription: str
    value: Optional[float]
    measure: Optional[str]
    date_purchase: Optional[datetime]
    date_expired: Optional[datetime]
