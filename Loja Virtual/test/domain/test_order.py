from src.domain.order import OrderStatus, OrderStatusName


def test_should_create_order():
    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED
    