from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Each model maps to a Mongo collection with the class name lowercased

class User(BaseModel):
    email: EmailStr
    password_hash: str
    name: Optional[str] = None
    role: str = "owner"

class Customer(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    notes: Optional[str] = None
    photo_url: Optional[str] = None

class Booking(BaseModel):
    customer_id: str
    date: str  # ISO date
    time: str  # HH:MM
    package: Optional[str] = None
    payment_status: str = Field(default="Pending")

class Payment(BaseModel):
    customer_id: Optional[str] = None
    amount: float
    method: str  # Cash, eSewa, Bank
    date: str
    notes: Optional[str] = None
    type: str = Field(default="income")  # income | expense

class Package(BaseModel):
    name: str
    price: float
    duration: Optional[str] = None
    included_items: Optional[List[str]] = None
    notes: Optional[str] = None

class Inventory(BaseModel):
    item_name: str
    category: Optional[str] = None
    quantity: int = 0
    condition: Optional[str] = None
    purchase_date: Optional[str] = None
    image_url: Optional[str] = None
