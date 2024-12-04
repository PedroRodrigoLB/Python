from src.domain.order import Order, OrderStatus, OrderStatusName, OrderItem
from src.domain.product import Product

def test_should_create_order():
    
    # Primeiro status: realizado
    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED
    
    product1: Product = Product(name="PS5", description="Produto bem legal", price= 5000)

    assert product1.name == "PS5"
    assert product1.description == "Produto bem legal"
    assert product1.price == 5000.0 

    product2: Product = Product(name="PS4", description="Produto com varios jogos", price= 3800)

    assert product2.name == "PS4"
    assert product2.description == "Produto com varios jogos"
    assert product2.price == 3800.0 

    product3: Product = Product(name="PS3", description="Produto para colecionadores", price= 8000)

    assert product3.name == "PS3"
    assert product3.description == "Produto para colecionadores"
    assert product3.price == 8000.0 

    item1: OrderItem = OrderItem(
        product_id=product1.id, price=product1.price, quantity=1
        )
    item2: OrderItem = OrderItem(
        product_id=product2.id, price=product2.price, quantity=2
        )
    
    order: Order = Order()
    order.add_status(status)
    order.add_item(item1)
    order.add_item(item2)
    
    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.items) == 2



    # novo status: em preparação
    status2 = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status2)

    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.IN_PREPARATION

    # novo status: enviado
    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status3)

    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SENT

    # novo status: entregue
    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)

    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED