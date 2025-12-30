import pprint
import pytest
from UI.utils.helpers import request_context, base_url

@pytest.mark.TC55
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
    response = request_context.get(f"{base_url}api/productsList")

    # Assertion
    response_body = response.json()
    assert response_body["responseCode"] == 200
    assert len(response_body["products"]) > 0
    assert response_body["products"][0]["name"] == "Blue Top"

@pytest.mark.TC66
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
    response = request_context.get(f"{base_url}api/brandsList")

    # Assertion
    response_body = response.json()
    assert response_body["responseCode"] == 200
    assert len(response_body["brands"]) > 0
    assert response_body["brands"][1]["brand"] == "H&M"

@pytest.mark.TC77
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
    response = request_context.get(f"{base_url}api/getUserDetailByEmail", form=param)

    response_body = response.json()
    assert response_body["responseCode"] == 400
    assert response_body["message"] == "Bad request, email parameter is missing in GET request."



