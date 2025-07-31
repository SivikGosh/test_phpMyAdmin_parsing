from requests import Session
from tabulate import tabulate
from tqdm import tqdm

from .settings import Config
from .tables import TablePage
from .utils import (
    collect_payload,
    get_page_soup,
    get_page_url,
    parse_table_url,
)


def main() -> None:

    progress = tqdm(desc='Парсинг таблицы', unit=' страница')
    result = []

    with Session() as s:

        login_page = get_page_soup(s, Config.url)
        payload = collect_payload(login_page)

        main = get_page_soup(s, f'{Config.url}/index.php?route=/', payload)
        db_url = get_page_url(main, 'pma_navigation_tree_content', Config.db)

        db_page = get_page_soup(s, f'{Config.url}/{db_url}')

        table_url = get_page_url(db_page, 'tablesForm', Config.table)
        next_url = table_url

        while True:
            page = TablePage(get_page_soup(s, f'{Config.url}/{next_url}'))
            if not page.is_page_has_rows():
                break
            page_result = page.get_result()
            result.extend(page_result)
            next_url = parse_table_url(next_url, page.rows_num)
            progress.update(1)
        progress.close()

    print(tabulate(result, 'keys', 'rounded_outline'))


if __name__ == '__main__':
    main()
