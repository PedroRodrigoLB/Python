# Sistema de Pedidos

- Customer
    nome
    email

- Product
    name
    description
    price

- Order
    [OrderStatus]
    [OrderItem]
    total

- OrderStatus
    nome (REALIZADO, EM PREPARACAO, ENVIADO, ENTREGUE, FINALIZADO)

- OrderItem
    - product_id
    - price
    - quantity