
def test_get_all_products(api_request):

    URL = "https://automationexercise.com/api/productsList"

    response = api_request.get(URL)

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    products = response_json["products"]

    assert isinstance(products, list)

    for product in products:
        assert "id" in product
        assert isinstance(product["id"], int)

        assert "name" in product
        assert isinstance(product["name"], str)

        assert "price" in product
        assert isinstance(product["price"], str)

        assert "brand" in product
        assert isinstance(product["brand"], str)

        assert "category" in product
        assert isinstance(product["category"], dict)

        assert "usertype" in product["category"]
        assert isinstance(product["category"]["usertype"], dict)
        
        assert "category" in product["category"]
        assert isinstance(product["category"]["category"], str)

