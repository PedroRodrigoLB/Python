from src.domains.customer import Customer


def test_should_create_customer():
    customer: Customer = Customer(
        name="Rodrigo", 
        email="rodrigo@test.com"
    )

    assert customer.name == "Rodrigo"
    assert customer.email == "rodrigo@test.com"