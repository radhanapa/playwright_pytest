import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "post_id, expected_user_id", [(1, 1), (2, 1), (11, 2), (21, 3)]
)
def test_validate_post_owners(api_client, post_id, expected_user_id):
    """Runs 4 times with different data points automatically."""
    response = api_client.get_post(post_id)
    expect(response).to_be_ok()

    payload = response.json()
    assert payload["userId"] == expected_user_id
