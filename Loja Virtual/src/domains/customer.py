from pydantic import BaseModel
from src.domains.base import DomainBase


class Customer(DomainBase):
    name: str
    email: str

class CustomerRegistration(BaseModel):
    name: str
    email: str
    password: str
    confirm_password: str