from requests import Session
from tabulate import tabulate

from .settings import Config
from .tables import TablePage
from .utils import collect_payload, get_page_soup, get_page_url


def main() -> None:
    with Session() as s:

        login_page = get_page_soup(s, Config.url)
        payload = collect_payload(login_page)

        main = get_page_soup(s, f'{Config.url}/index.php?route=/', payload)
        db_url = get_page_url(main, 'pma_navigation_tree_content', Config.db)

        db_page = get_page_soup(s, f'{Config.url}/{db_url}')
        table_url = get_page_url(db_page, 'tablesForm', Config.table)

        table_page = TablePage(get_page_soup(s, f'{Config.url}/{table_url}'))
        result = table_page.get_result()

        print(tabulate(result, 'keys', 'rounded_outline'))


if __name__ == '__main__':
    main()
