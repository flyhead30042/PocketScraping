
from pocket_scraping import postman
import json
import logging

URL = "https://getpocket.com/v3/oauth/request"
HEADERS= {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
          "X-Accept": "application/json"}
POSTDATA = {"consumer_key": "74406-8a08d271e96900d77476c4dc", "redirect_uri":"http://www.google.com"}
DATA={}

if __name__ == "__main__":

    # api = postman.WebAPI()
    # api.postAPI(URL, HEADERS, POSTDATA)
    # d = json.loads(api.resp.text)
    #
    # for k in d.keys():
    #     logging.debug("%s:%s" %(k, d[k]))


    api = postman.WebAPI()
    api.postAPI("https://getpocket.com/v3/get",
                {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "X-Accept": "application/json"},
                {"consumer_key":"74406-8a08d271e96900d77476c4dc", "access_token":"0ea8699b-2a3c-8391-9cdd-561517"})


    d = json.loads(api.resp.text)
    for k in d.keys():
        logging.debug("%s:%s" %(k, d[k]))
