import pytest
import allure
from playwright.sync_api import expect


# This will run the test 3 times with different IDs
@pytest.mark.api
@pytest.mark.integration
@allure.feature("Posts API")
@pytest.mark.parametrize(
    "post_id, expected_title",
    [
        (
            1,
            "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        ),
        (2, "qui est esse"),
        (3, "ea molestias quasi exercitationem repellat qui ipsa sit aut"),
    ],
)
def test_get_multiple_posts(api_client, post_id, expected_title):
    response = api_client.get_post(post_id)

    expect(response).to_be_ok()
    payload = response.json()

    assert payload["id"] == post_id
    assert payload["title"] == expected_title
