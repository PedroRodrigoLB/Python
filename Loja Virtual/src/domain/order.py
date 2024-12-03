from pydantic import BaseModel, Field
from src.domain.base import DomainBase
from enum import Enum


class OrderStatusName(str,Enum):
    ACCOMPLISHED = "realizado"
    IN_PREPARATION = "em preparação"
    SENT = "enviado"
    DELIVERED = "entregue"
    FINISHED = "finalizado"


class OrderStatus(BaseModel):
    name: OrderStatusName = Field(default=OrderStatusName.ACCOMPLISHED)


class OrderItem(BaseModel):
    product_id: int
    price: float
    quantity: int


class Order(DomainBase):
    status: list[OrderStatus] = Field(default=[])
    item: list[OrderItem] = Field(default=[])