import pprint
import pytest
from UI.utils.helpers import request_context, base_url
from UI.utils.helpers import generate_random_email


@pytest.mark.TC11
def test_register_new_user_account(request_context):
    """
     Test Case: Register a new user account
     Description:
     This test sends a POST request to the 'createAccount'
     API endpoint to register a new user.
     A random email is generated to avoid duplicate
     registration conflicts.

    :param request_context:
    :return:
    """
    form_data = {
        "name": "investor",
        "email": generate_random_email(),
        "password": "tester2025#",
        "title": "",
        "birth_date": "",
        "birth_month": "",
        "birth_year": "",
        "firstname": "Sulaimon",
        "lastname": "Ekundayo",
        "company": "",
        "address1": "44, Main Str",
        "address2": "",
        "country": "India",
        "zipcode": "2345",
        "state": "Delhi",
        "city": "Delhi",
        "mobile_number": "447788990022"
    }

    response = request_context.post(f"{base_url}api/createAccount", form=form_data)

    response_body = response.json()
    assert response_body["responseCode"] == 201
    assert response_body["message"] == "User created!"


@pytest.mark.TC22
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
    response = request_context.post(f"{base_url}api/productsList")

    response_body = response.json()
    assert response_body["responseCode"] == 405
    assert response_body["message"] == "This request method is not supported."

@pytest.mark.TC33
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
        f"{base_url}api/searchProduct",
        form=payload
    )
    response_body = response.json()
    assert response_body["responseCode"] == 200
    assert len(response_body["products"]) > 0

@pytest.mark.TC44
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
        "email": "tester_245@mail.com",
        "password": "tester2025#"
    }
    response = request_context.post(f"{base_url}api/verifyLogin", form=params)

    response_body = response.json()
    assert response_body["responseCode"] == 200
    assert response_body["message"] == "User exists!"






