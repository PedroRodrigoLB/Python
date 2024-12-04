# Sistema de Pedidos

<h3>Customer</h3>
    <ul type="square">
        <li>nome</li>
        <li>email</li>
    </ul>

<h3>Product</h3>
    <ul type="square">
        <li>name</li>
        <li>description</li>
        <li>price</li>
    </ul>

<h3>Order</h3>
    <ul type="square">
        <li>[OrderStatus]</li>
        <li>[OrderItem]</li>
        <li>total</li>
    </ul>

<h3>OrderStatus</h3>
    <ul type="square">
        <li>nome (REALIZADO, EM PREPARACAO, ENVIADO, ENTREGUE, FINALIZADO)</li>
    </ul>

<h3>OrderItem</h3>
    <ul type="square">
        <li>product_id</li>
        <li>price</li>
        <li>quantity</li>
    </ul>