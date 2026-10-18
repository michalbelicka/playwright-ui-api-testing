
def test_put_all_brands(api_request):

    URL = "https://automationexercise.com/api/brandsList"

    response = api_request.put(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 405

    assert response_json["message"] == "This request method is not supported."