from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from schemas import Customer, Booking, Payment, Package, Inventory
from database import create_document, get_documents

app = FastAPI(title="StudioLedger API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Msg(BaseModel):
    message: str

@app.get("/test", response_model=Msg)
async def test():
    return {"message": "ok"}

# Customers
@app.post("/customers")
async def create_customer(payload: Customer):
    doc = await create_document("customer", payload.model_dump())
    return doc

@app.get("/customers")
async def list_customers():
    docs = await get_documents("customer", {}, 200)
    return docs

# Bookings
@app.post("/bookings")
async def create_booking(payload: Booking):
    doc = await create_document("booking", payload.model_dump())
    return doc

@app.get("/bookings")
async def list_bookings():
    docs = await get_documents("booking", {}, 200)
    return docs

# Payments (income & expense)
@app.post("/payments")
async def create_payment(payload: Payment):
    doc = await create_document("payment", payload.model_dump())
    return doc

@app.get("/payments")
async def list_payments():
    docs = await get_documents("payment", {}, 200)
    return docs

# Packages
@app.post("/packages")
async def create_package(payload: Package):
    doc = await create_document("package", payload.model_dump())
    return doc

@app.get("/packages")
async def list_packages():
    docs = await get_documents("package", {}, 200)
    return docs

# Inventory
@app.post("/inventory")
async def create_item(payload: Inventory):
    doc = await create_document("inventory", payload.model_dump())
    return doc

@app.get("/inventory")
async def list_inventory():
    docs = await get_documents("inventory", {}, 200)
    return docs
