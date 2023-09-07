from common import config
import requests
import bs4


class NewsPage:
    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._url = url
        self._visit(url)

    def _visit(self, url):
        '''
        Obtener el texto o contenido HTML del sitio web en texto plano
        '''
        # HOTFIX: este header es solo para evitar el error:  requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://www.eluniversal.com.mx/
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        
        response = requests.get(url, headers = headers)
        response.raise_for_status() # imprime mensaje por consola o terminal si hay algun codigo de error como respuesta
        
        # retorna un objeto de beautiful soup
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
    
    def _select(self, query_string):
        '''
        Funcion para seleccionar los elementos que necesitamos del sitio web
        '''
        return self._html.select(query_string)

class HomePage(NewsPage):
    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

class ArticlePage(NewsPage):
    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def body(self):
        result = self._select(self._queries['article_body'])

        return result[0].text if len(result) else ''

    @property
    def title(self):
        result = self._select(self._queries['article_title'])

        return result[0].text if len(result) else ''
    
    @property
    def url(self):
        return self._url