import jwt
from jwt.exceptions import DecodeError

from meier.exc import TokenCreateError, TokenParseError


class TokenInfo:
    def __init__(
        self, email: str, user_name: str, blog_title: str, profile_image=None
    ) -> None:
        self.email = email
        self.user_name = user_name
        self.blog_title = blog_title
        self.profile_image = profile_image
        self.iss = "MEIER"
        self.aud = "MEIER"

    def to_dict(self) -> dict:
        return vars(self)


def create_token(token_info: TokenInfo) -> str:
    try:
        if not isinstance(token_info, TokenInfo):
            raise TokenCreateError
        return jwt.encode(token_info.to_dict(), "meire_ppp", algorithm="HS256")

    except (ValueError, TypeError):
        raise TokenCreateError


def parse_token(token: str):
    try:
        return jwt.decode(
            jwt=token,
            key="meire_ppp",
            algorithms=["HS256"],
            subject="MEIER",
            audience="MEIER",
        )
    except DecodeError:
        raise TokenParseError
