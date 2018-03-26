import requests
import logging



class WebAPI(object):
    def __init__(self):
        self.resp = None

    def postAPI(self, url, headers=None, postdata=None):

        r = requests.post(url=url, headers=headers, data=postdata)
        logging.debug("Request %s ==> response (%s)[%s]" % (r.url, r.status_code, r.text))
        try:
            r.raise_for_status()
            self.resp = r
        except Exception as err:
            logging.error("(%s)(%s)(%s):[%s]" %(r.status_code, r.headers["X-Error-Code"], r.headers["X-Error"], err))


