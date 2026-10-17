import pytest

@pytest.mark.parametrize("email, password, expected_response_code, expected_message",
                         [
                             (
                                 "tester2310@example.com",
                                 "password",
                                 200,
                                 "User exists!"
                             ),
                             (
                                 "invalid@email.com",
                                 "invalidpassword",
                                 404,
                                 "User not found!"
                             )
                         ])
def test_post_verify_login(api_request, email, password, expected_response_code, expected_message):

    URL = "https://automationexercise.com/api/verifyLogin"

    response = api_request.post(
        URL,
        form={
            "email": email,
            "password": password
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == expected_response_code

    assert response_json["message"] == expected_message

