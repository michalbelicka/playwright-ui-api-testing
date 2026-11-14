import pytest

@pytest.mark.parametrize("email, password, expected_response_code, expected_message",
                         [
                             pytest.param(
                                 "tester2310@example.com",
                                 "password",
                                 200,
                                 "User exists!",
                                 id="valid-email-and-password"
                             ),
                             pytest.param(
                                 "invalid@email.com",
                                 "invalidpassword",
                                 404,
                                 "User not found!",
                                 id="invalid-email-and-password"
                             ),
                             pytest.param(
                                 None,
                                 "password",
                                 400,
                                 "Bad request, email or password parameter is missing in POST request.",
                                 id="missing-email"
                             ),
                             pytest.param(
                                 "tester2310@example.com",
                                 None,
                                 400,
                                 "Bad request, email or password parameter is missing in POST request.",
                                 id="missing-password"
                             )
                         ])
def test_post_verify_login(api_request, email, password, expected_response_code, expected_message):

    URL = "https://automationexercise.com/api/verifyLogin"

    form = {}

    if email is not None:
        form["email"] = email

    if password is not None:
        form["password"] = password

    response = api_request.post(
        URL,
        form=form
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == expected_response_code

    assert response_json["message"] == expected_message

