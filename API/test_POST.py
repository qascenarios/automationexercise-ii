import pprint
import pytest
from UI.utils.helpers import request_context, base_url

def test_post_to_all_product_list(request_context):
    """
    # Test Case: POST request to Products List endpoint
    Description:
    This test sends a POST request to the 'productsList' API
    endpoint. Although the endpoint is primarily designed
    for GET requests, the API still responds with HTTP 200.
    The test verifies that the endpoint accepts the request
    and returns a successful response.

    :param request_context:
    :return:
    """
    response = request_context.post(f"{base_url}productsList")
    assert response.status == 200
    assert response.status_text == "OK"

def test_search_for_products(request_context):
    """
    Test Case: Search for products
    Description:
    This test sends a POST request to the 'searchProduct'
    endpoint with a search keyword as payload.
    It verifies that the API returns a successful response
    and prints the list of products matching the search term.

    :param request_context:
    :return:
    """
    payload = {
        "search_product": "jean",
    }

    response = request_context.post(
        f"{base_url}searchProduct",
        data=payload
    )

    assert response.status == 200
    pprint.pprint(response.json())

def test_verify_login_with_valid_credentials(request_context):
    """
    # Test Case: Verify login with credentials
    Description:
    This test sends a POST request to the 'verifyLogin'
    endpoint with email and password as query parameters.
    The API always returns HTTP 200, while the actual
    success or failure is indicated inside the response body.
    his test verifies the HTTP response and prints the
    returned message for validation.

    :param request_context:
    :return:
    """

    params = {
        "email": "test_245@mail.com",
        "password": "tester2025#"
    }
    response = request_context.post(f"{base_url}verifyLogin", params=params)
    assert response.status == 200

    pprint.pprint(response.json())


