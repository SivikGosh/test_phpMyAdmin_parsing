from os import getenv

from dotenv import load_dotenv

from .utils import parse_args

load_dotenv()

args = parse_args()


class Config:
    url = getenv('URL')
    login = getenv('LOGIN')
    password = getenv('PASSWORD')
    db = args.db
    table = args.table
