from meier.app import create_app
from meier.config import Config

app = create_app(config=Config())
