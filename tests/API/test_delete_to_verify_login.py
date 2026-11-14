
def test_delete_to_verify_login(api_request):

    URL = "https://automationexercise.com/api/verifyLogin"

    response = api_request.delete(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 405

    assert response_json["message"] == "This request method is not supported."

    