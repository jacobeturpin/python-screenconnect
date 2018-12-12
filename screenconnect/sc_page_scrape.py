"""Class to handle page scraping functionality"""

from bs4 import BeautifulSoup


VIEW_STATE_ID = '__VIEWSTATE'
VIEW_STATE_GEN_ID = '__VIEWSTATEGENERATOR'


class ScPageScraper:

    def __init__(self):

        self.view_state = None
        self.view_state_generator = None
        self.page_content = dict()

    @property
    def page_state_payload(self):
        payload = {
            '__LASTFOCUS': None,
            '__EVENTTARGET': None,
            '__EVENTARGUMENT': None,
            VIEW_STATE_ID: self.view_state,
            VIEW_STATE_GEN_ID: self.view_state_generator
        }
        payload.update(self.page_content)
        return payload

    def _get_page_state(self, content, page_ids):
        """Takes HTML content and scrapes for .NET ASPX page state

        Args:
            content (str): text-based HTML input
            page_ids (list): iteration of page-specific strings to find

        """
        self.page_content = dict()
        soup = BeautifulSoup(content)

        for page_id in page_ids + [VIEW_STATE_ID, VIEW_STATE_GEN_ID]:
            element = soup.find('input', {'id': page_id}).attrs.get('name')
            self.page_content[element.attrs.get('name')] = element.attrs.get('value')
