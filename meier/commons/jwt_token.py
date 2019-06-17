import jwt


class TokenInfo(object):
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
        if isinstance(token_info, TokenInfo):
            return jwt.encode(
                token_info.to_dict(), "meire_ppp", algorithm="HS256"
            )
    except Exception as e:
        raise e


def parse_token(token: str):
    try:
        return jwt.decode(
            token,
            "meire_ppp",
            algorithm="HS256",
            subject="MEIER",
            audience="MEIER",
        )
    except Exception as e:
        raise e
