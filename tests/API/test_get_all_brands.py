
def test_get_all_brands(api_request):

    URL = "https://automationexercise.com/api/brandsList"

    response = api_request.get(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    assert "brands" in response_json

    brands = response_json["brands"]

    assert isinstance(brands, list)

    for brand in brands:
        assert "id" in brand
        assert isinstance(brand["id"], int)

        assert "brand" in brand
        assert isinstance(brand["brand"], str)
        assert brand["brand"].strip() != ""
    