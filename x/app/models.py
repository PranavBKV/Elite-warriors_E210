from pydantic import BaseModel

class VendorProfile(BaseModel):
    business_type: str
    monthly_budget: int
    inventory_type: str
    staff_count: int
    customer_flow: str
    online_presence: str
