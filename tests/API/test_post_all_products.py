
def test_post_all_products(api_request):

    URL = "https://automationexercise.com/api/productsList"

    response = api_request.post(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 405

    assert response_json["message"] == "This request method is not supported."