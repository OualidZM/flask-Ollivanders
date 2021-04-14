import pytest
from app import app


@pytest.mark.get_item
def test_get_aged_brie():
    test = app.test_client()
    response = test.get("/item/Aged Brie")
    assert b'{"name":"Aged Brie"' in response.data


@pytest.mark.get_item_fail
def test_get_aged_brie_fail():
    test = app.test_client()
    response = test.get("/item/Aged Brie2")
    assert b'{"none":"null"' in response.data
