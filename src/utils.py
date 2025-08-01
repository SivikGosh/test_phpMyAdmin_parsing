from argparse import ArgumentParser, Namespace
from re import compile
from typing import Dict
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from bs4 import BeautifulSoup
from requests import Session


def get_page_soup(
    session: Session,
    url: str,
    payload: Dict[str, str] = None
) -> BeautifulSoup:
    page = session.post(url, payload) if payload else session.get(url)
    return BeautifulSoup(page.text, 'html.parser')


def collect_payload(
    page: BeautifulSoup,
    login: str,
    password: str
) -> Dict[str, str]:
    return {
        'set_session': page.find(attrs={'name': 'set_session'})['value'],
        'pma_username': login,
        'pma_password': password,
        'server': 1,
        'token': page.find(attrs={'name': 'token'})['value'],
    }


def get_page_url(
    page: BeautifulSoup,
    element_id: str,
    element_name: str
) -> str:
    return (
        page
        .find(attrs={'id': element_id})
        .find('a', string=compile(element_name))
        .get('href')
    )


def parse_table_url(url: str, pos: str) -> None:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    query['pos'][0] = int(query['pos'][0]) + pos
    new_query = urlencode(query, doseq=True)
    new_url = urlunparse(parsed._replace(query=new_query))
    return new_url


def parse_args() -> Namespace:
    parser = ArgumentParser(description='Парсинг phpMyAdmin таблицы')
    parser.add_argument('--db', required=True, help='Имя базы данных')
    parser.add_argument('--table', required=True, help='Имя таблицы')
    return parser.parse_args()
