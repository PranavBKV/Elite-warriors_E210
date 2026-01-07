from fastapi import FastAPI
from app.models import VendorProfile
from app.logic import final_advice

app = FastAPI(title="Virtual Business Growth Manager")

@app.post("/business-advice")
def business_advice(profile: VendorProfile):
    return final_advice(profile)
