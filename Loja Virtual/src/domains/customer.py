from src.domains.base import DomainBase


class Customer(DomainBase):
    name: str
    email: str