from typing import Dict, List

from bs4 import BeautifulSoup


class TablePage:
    def __init__(self, page: BeautifulSoup) -> None:
        self.page = page
        self.table = self._get_table()
        self.titles = self._get_titles()
        self.rows = self._get_rows()
        self.rows_num = self._get_selected_rows_num()
    
    def _get_table(self) -> str:
        return self.page.find(attrs={'class': 'data'})
    
    def _get_titles(self) -> List[str]:
        return list(
            title['data-column'] for title
            in self.table.find_all('th', attrs={'data-column': True})
        )
    
    def _get_rows(self) -> List[str]:
        return list(
            row.text for row
            in self.table.find_all('td', attrs={'data-decimals': True})
        )
    
    def _get_selected_rows_num(self) -> int:
        rows_num = (
            self.page
            .find(attrs={'id': 'sessionMaxRowsSelect'})
            .find('option', selected=True).text.strip()
        )
        return int(rows_num)
    
    def get_result(self) -> List[Dict[str, str]]:
        result = []
        t, r = len(self.titles), len(self.rows)
        for i in range(0, r, t):
            result.append(
                dict(zip(self.titles, self.rows[i:i+t]))
            )
        return result

    def is_page_has_rows(self) -> None:
        return True if len(self.rows) > 0 else False
