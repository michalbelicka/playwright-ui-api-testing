import random

def test_delete_account(api_request):

    URL_POST = "https://automationexercise.com/api/createAccount"
    URL_DELETE = "https://automationexercise.com/api/deleteAccount"
    URL_GET = "https://automationexercise.com/api/getUserDetailByEmail"

    payload = {
            "email": f"random_tester{random.randint(1000, 9999)}@example.com",
            "password": "password",
            "name": f"randomname{random.randint(500, 9999)}",
            "firstname": "test user",
            "lastname": "test user",
            "address1": "test address",
            "country": "test country",
            "state": "test state",
            "city": "test city",
            "zipcode": "zipcode",
            "mobile_number": "mobile_number"
    }

    response = api_request.post(
        URL_POST,
        form=payload
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 201

    assert response_json["message"] == "User created!"

    response = api_request.delete(
        URL_DELETE,
        form={
            "email": payload["email"],
            "password": payload["password"]
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    assert response_json["message"] == "Account deleted!"

    response = api_request.get(
        URL_GET,
        params={"email": payload["email"]}
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 404

    assert response_json["message"] == "Account not found with this email, try another email!"


    