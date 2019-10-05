import pytest

from meier.commons.jwt_token import TokenInfo, create_token, parse_token
from meier.exc import TokenCreateError, TokenParseError


def test_token_info():
    token_info = TokenInfo("email@gmail.com", "user_name", "blog_title")
    assert token_info.email == "email@gmail.com"
    assert token_info.user_name == "user_name"
    assert token_info.blog_title == "blog_title"

    assert token_info.to_dict() == {
        "email": "email@gmail.com",
        "user_name": "user_name",
        "blog_title": "blog_title",
        "profile_image": None,
        "iss": "MEIER",
        "aud": "MEIER",
    }


def test_create_token():
    token_info = TokenInfo("email@gmail.com", "user_name", "blog_title")
    assert len(create_token(token_info)) > 0
    with pytest.raises(TokenCreateError):
        create_token("test")


def test_parse_token():
    token_info = TokenInfo("email@gmail.com", "user_name", "blog_title")
    token = create_token(token_info)
    parsed = parse_token(token)

    assert parsed["user_name"] == "user_name"
    assert parsed["email"] == "email@gmail.com"
    assert parsed["blog_title"] == "blog_title"

    with pytest.raises(TokenParseError):
        parse_token("test")
