from pydantic import BaseModel

class VendorProfile(BaseModel):
    business_type: str          # kirana, tea shop, clothing, etc.
    monthly_budget: int         # ₹ per month
    inventory_type: str         # fast / slow / seasonal
    staff_count: int            # number of people
    customer_flow: str          # walk-in / mixed / online
    online_presence: str        # instagram / whatsapp / none
