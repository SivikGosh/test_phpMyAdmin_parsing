from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    url = getenv('URL')
    login = getenv('LOGIN')
    password = getenv('PASSWORD')
    db = getenv('DB')
    table = getenv('TABLE')
