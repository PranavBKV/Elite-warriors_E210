from dataclasses import dataclass
from typing import List

@dataclass
class VendorInput:
    business_type: str                 # kirana, clothing, electronics
    monthly_budget: int               # INR
    inventory_level: str              # low / medium / high
    staff_count: int
    online_presence: List[str]        # ["Instagram", "WhatsApp"] or []
    daily_walkins: bool
