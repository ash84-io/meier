from meier_app.commons.jwt_token import TokenInfo, create_token, parse_token


def test_create_parse_token():
    test_token = TokenInfo(
        email="test@test.co.kr",
        user_name="test",
        blog_title="test",
        profile_image="test",
    )

    token = create_token(token_info=test_token)
    token_dict = parse_token(token)
    assert token_dict["email"] == "test@test.co.kr"
    assert token_dict["user_name"] == "test"
    assert token_dict["blog_title"] == "test"
    assert token_dict["profile_image"] == "test"

    none_token = TokenInfo(
        email=None, user_name=None, blog_title=None, profile_image=None
    )

    token = create_token(token_info=none_token)
    token_dict = parse_token(token)

    assert token_dict["email"] is None
    assert token_dict["user_name"] is None
    assert token_dict["blog_title"] is None
    assert token_dict["profile_image"] is None
