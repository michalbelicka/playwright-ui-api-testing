
def test_post_search_product_without_search_product_parameter(api_request):

    URL = "https://automationexercise.com/api/searchProduct"

    response = api_request.post(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 400

    assert response_json["message"] == "Bad request, search_product parameter is missing in POST request."