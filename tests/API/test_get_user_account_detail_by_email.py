
def test_get_user_account_detail_by_email(api_request, created_account):

    URL = "https://automationexercise.com/api/getUserDetailByEmail"

    response = api_request.get(
        URL,
        params={
            "email": created_account["email"]
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    user = response_json["user"]

    assert isinstance(user, dict)

    assert isinstance(user["id"], int)
    
    assert user["name"] == created_account["name"]
    assert user["email"] == created_account["email"]
    assert user["first_name"] == created_account["firstname"]
    assert user["last_name"] == created_account["lastname"]
    assert user["address1"] == created_account["address1"]
    assert user["country"] == created_account["country"]
    assert user["state"] == created_account["state"]
    assert user["city"] == created_account["city"]
    assert user["zipcode"] == created_account["zipcode"]
    




    