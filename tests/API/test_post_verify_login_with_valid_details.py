
def test_post_verify_login_with_valid_details(api_request):

    URL = "https://automationexercise.com/api/verifyLogin"

    response = api_request.post(
        URL,
        form={
            "email": "tester2310@example.com",
            "password": "password"
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    assert response_json["message"] == "User exists!"