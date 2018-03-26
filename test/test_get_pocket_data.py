from pocket_scraping.pocketman import *
import json
import logging

if __name__ == "__main__":

    l = get_pocket_data(consumer_key="74406-8a08d271e96900d77476c4dc",
                        access_token="0ea8699b-2a3c-8391-9cdd-561517",
                        **{"tag": "python", "detailType": "complete"})

    logging.debug("Total %i items" %(len(l)))
