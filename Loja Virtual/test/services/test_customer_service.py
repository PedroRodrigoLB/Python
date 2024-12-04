
from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration
import pytest


@pytest.mark.asyncio
async def test_should_creat_customer():

    service = CustomerFactory.create_mock()

    customer = CustomerRegistration(
        name = "Rodrigo",
        email= "rodrigo@test.com",
        password = "123456",
        confirm_password ="123456",
    )

    response = await service.register(customer_registration=customer)

    print(response)