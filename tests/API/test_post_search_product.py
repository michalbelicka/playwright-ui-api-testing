
def test_post_search_product(api_request):

    URL = "https://automationexercise.com/api/searchProduct"

    response = api_request.post(
        URL,
        form={"search_product": "top"}
    )

    assert response.status == 200

    response_json = response.json()

    assert response_json["responseCode"] == 200

    products = response_json["products"]

    assert isinstance(products, list)

    for product in products:

        assert "Top" in product["name"] or "Shirt" in product["name"]

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