import pprint
import pytest
from UI.utils.helpers import request_context, base_url


def test_get_all_products_list(request_context):
    """
    Test Case: Get All Products List
    Description:
    This test sends a GET request to the 'productsList' API
    endpoint and verifies that the API responds successfully.
    It validates that the response status code is 200 (OK)
    and prints the returned list of products.

    :param request_context:
    :return:
    """
    response = request_context.get(f"{base_url}productsList")

    # Assertion
    assert response.ok
    assert response.status == 200

    response_body = response.json()
    pprint.pprint(response_body)

def test_get_all_brands_list(request_context):
    """
    Test Case: Get All Brands List
    Description:
    This test sends a GET request to the 'brandsList' API
    endpoint and verifies that the API responds successfully.
    It confirms that the response status code is 200 (OK)
    and prints the returned list of brands.

    :param request_context:
    :return:
    """
    response = request_context.get(f"{base_url}brandsList")

    # Assertion
    assert response.ok
    assert response.status == 200

    response_body = response.json()
    pprint.pprint(response_body)

def test_get_user_account_details(request_context):
    """
    Test Case: Get User Account Details by Email
    Description:
    This test sends a GET request to the 'getUserDetailByEmail'
    API endpoint to retrieve user account details using an
    email parameter. It verifies that the API responds
    successfully with status code 200 and prints the user data.

    :param request_context:
    :return:
    """
    param = {"email": "test_245@mail.com"}
    response = request_context.get(f"{base_url}getUserDetailByEmail", params=param)
    assert response.ok
    assert response.status == 200

    pprint.pprint(response.json())


