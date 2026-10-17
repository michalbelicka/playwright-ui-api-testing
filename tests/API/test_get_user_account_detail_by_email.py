
def test_get_user_account_detail_by_email(api_request):

    URL = "https://automationexercise.com/api/getUserDetailByEmail"

    response = api_request.get(
        URL,
        params={
            "email": "tester2310@example.com"
        }
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    user = response_json["user"]

    assert isinstance(user, dict)

    assert user["id"] == 2893308
    assert isinstance(user["id"], int)
    
    assert user["name"] == "Tester2310"
    assert user["email"] == "tester2310@example.com"
    assert user["title"] == "Mr"
    assert user["birth_day"] == "10"
    assert user["birth_month"] == "10"
    assert user["birth_year"] == "10"
    assert user["first_name"] == "Tester"
    assert user["last_name"] == "Testing"
    assert user["company"] == "test"
    assert user["address1"] == "Street address"
    assert user["address2"] == ""
    assert user["country"] == "Canada"
    assert user["state"] == "California"
    assert user["city"] == "Los Angeles"
    assert user["zipcode"] == "90001"




    