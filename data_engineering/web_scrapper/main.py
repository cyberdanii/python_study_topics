import argparse
import logging
from common import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _news_scrapper(news_site_uid):
    host = config()['news_sites'][news_site_uid]["url"]
    logging.info("Beginning scrapper for {}".format(host))

if  __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = config()['news_sites'].keys()
    parser.add_argument("news_site", help="The news site that you want to scrape", type=str, choices=news_site_choices)

    args =  parser.parse_args()
    _news_scrapper(args.news_site)