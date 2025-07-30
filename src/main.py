# from bs4 import BeautifulSoup
from re import compile

from bs4 import BeautifulSoup
from requests import Session
from tabulate import tabulate

from .settings import Config


def main() -> None:
    with Session() as s:

        login_page = s.get(Config.url)
        login_soup = BeautifulSoup(login_page.text, 'html.parser')
        token = login_soup.find(attrs={'name': 'token'})
        set_session = login_soup.find(attrs={'name': 'set_session'})
        payload = {
            'set_session': set_session['value'],
            'pma_username': Config.login,
            'pma_password': Config.password,
            'server': '1',
            'token': token['value'],
        }

        admin_page = s.post(f'{Config.url}/index.php?route=/', data=payload)
        admin_soup = BeautifulSoup(admin_page.text, 'html.parser')
        links = admin_soup.find(attrs={'id': 'pma_navigation_tree_content'})
        db_page_url = links.find('a', string=Config.db).get('href')

        db_page = s.get(f'{Config.url}/{db_page_url}')
        db_soup = BeautifulSoup(db_page.text, 'html.parser')
        table_form = db_soup.find(attrs={'id': 'tablesForm'})
        table_url = (
            table_form.find('a', string=compile(Config.table)).get('href')
        )

        table_page = s.get(f'{Config.url}/{table_url}')
        table_soup = BeautifulSoup(table_page.text, 'html.parser')

        # selected_rows = int(
        #     table_soup
        #     .find(attrs={'id': 'sessionMaxRowsSelect'})
        #     .find('option', selected=True).text.strip()
        # )

        result_form = table_soup.find(attrs={'name': 'resultsForm'})
        result_table = result_form.find('table')
        titles = [
            title['data-column'] for title
            in result_table.find_all('th', attrs={'data-column': True})
        ]
        data = [
            row.text for row
            in result_table.find_all('td', attrs={'data-decimals': True})
        ]
        n = len(titles)
        result = [
            dict(zip(titles, data[i:i+n])) for i in range(0, len(data), n)
        ]
        res = tabulate(result, 'keys', 'rounded_outline')
        print(res)


if __name__ == '__main__':
    main()
