
def test_update_user_account(api_request, created_account):

    URL_UPDATE = "https://automationexercise.com/api/updateAccount"
    URL_GET = "https://automationexercise.com/api/getUserDetailByEmail"

    updated_payload = {
        "email": created_account["email"],
        "password": created_account["password"],
        "name": "updated name",
        "firstname": "updated user",
        "lastname": "updated user",
        "address1": "updated address",
        "country": "updated country",
        "state": "updated state",
        "city": "updated city",
        "zipcode": "updated zipcode",
    }

    response = api_request.put(
        URL_UPDATE,
        form=updated_payload
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    assert response_json["message"] == "User updated!"

    response = api_request.get(
        URL_GET,
        params={
            "email": created_account["email"]
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    user = response_json["user"]

    assert isinstance(user, dict)

    assert user["email"] == updated_payload["email"]
    assert user["name"] == updated_payload["name"]
    assert user["first_name"] == updated_payload["firstname"]
    assert user["last_name"] == updated_payload["lastname"]
    assert user["address1"] == updated_payload["address1"]
    assert user["country"] == updated_payload["country"]
    assert user["state"] == updated_payload["state"]
    assert user["city"] == updated_payload["city"]
    assert user["zipcode"] == updated_payload["zipcode"]

 


