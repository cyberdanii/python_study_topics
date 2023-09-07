import re
import csv
import logging
import argparse
from common import config
from datetime import datetime as dt
import news_page_objects as page_retriever

# Clases de librerias para manejar errores
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

# modulo para imprimir mejores mensajes por la terminal
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# expresiones regulares para valdiar si las URl o enalces estan formados correctamente
is_well_formed_link = re.compile(r'^https?://.+/.+$') # ejemplo de una conincidencia: https://www.google.com/example-text
is_root_path =  re.compile(r'^/.+$') # ejemplo de una coincidencia: /example-text


def _news_scrapper(news_site_uid: str):
    '''
    Funcion para extraer la URL del sitio indicado  por la terminal de usuario
    '''

    site_url = config()['news_sites'][news_site_uid]["url"] # se busca la url que coincide con la clave o key indicada
    logging.info("\n- - - - \nBeginning scrapper for {} 🎇\n- - - - ".format(site_url))
    homepage = page_retriever.HomePage(news_site_uid, site_url)

    # # imprimir los links
    # for link in homepage.article_links:
    #     print(link)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, site_url, link)

        if article:
            # logger.info('\n~ ~ ~ ~ \nArticle fetched\n~ ~ ~ ~ ')
            logger.info('✔️')
            articles.append(article)
            # print(article.title)

        # print(len(articles))
    logging.info('Data retrieved successfully ☑️')
    _save_articles(news_site_uid, articles)

def _save_articles(news_site_uid, articles):
    '''
    Funcion para guardar la informacion en un archivo csv
    '''
    now = dt.now().date()
    file_name = f'{news_site_uid}_{now}_articles.csv'

    # retorna ['title','body']
    csv_headers = list(
        filter(
            lambda property: not property.startswith('_'), dir(articles[0])
        )
    )

    with open(file_name, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

        for article in articles:
            # how to use getattr: https://www.w3schools.com/python/ref_func_getattr.asp
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)
    logging.info('Data saved successfully ✅🗄️')

def _fetch_article(news_site_uid, host, link):
    '''
    Funcion para extraer los articulos utilizando la clase en news_page_objects
    '''
    # logger.info('Start fetching article ar {}'.format(link))

    article =  None
    try:
        article = page_retriever.ArticlePage(news_site_uid, _build_link(host, link))
    except (HTTPError, MaxRetryError) as ex:
        # logger.warn('Error while fetching article!', exc_info=False)
        logger.warning('⚠️', exc_info=False)
    
    # validar si el articulo tiene cuerpo o body
    if article and not article.body:
        # logger.warn('Invalid article. There is no body.')
        return None
    
    return article

def _build_link(host, link):
    '''
    Funcion para validar si la URl o link es correcto o esta bien formado
    '''
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    else:
        return '{host}/{path}'.format(host = host, path = link)
        

# inicio de ejecucion del programa
if  __name__ == '__main__':
    
    parser = argparse.ArgumentParser()

    # obtener las llaves del diccionario u objeto por nombre 'news_sites'
    news_site_choices = list(config()['news_sites'].keys())

    parser.add_argument("news_site", # nombre de la clave o llave que contendra el valor que inserte el usuario por la terminal
                        help="The news site that you want to scrape", # texto o mensaje en la terminal para el usuario
                        type=str, # define el tipo de dato que se va recibir
                        choices=news_site_choices) # define las opciones disponibles que puede insertar el usuario por la terminal

    args =  parser.parse_args() # convierte los argumentos en un objeto
    

    _news_scrapper(args.news_site)