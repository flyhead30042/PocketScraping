from pocket_scraping import postman
import logging
import json

api = postman.WebAPI()

# 1) OBTAIN A REQUEST TOKEN BY USING CONSUMER KEY
def get_request_token():
    logging.info("=== OBTAIN A REQUEST TOKEN ===")
    api.postAPI("https://getpocket.com/v3/oauth/request",
                         {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", "X-Accept": "application/json"},
                         {"consumer_key": "74406-8a08d271e96900d77476c4dc", "redirect_uri":"http://www.google.com"})

    d = json.loads(api.resp.text)
    # return request token
    return d["code"]


# 2)  VISIT THE POCKET WEBSITE TO AUTHORIZE YOUR APP TO BIND THE CONSUMER KEY AND THE USER

# 3) CONVERT YOUR REQUEST TOKEN INTO A POCKET ACCESS TOKEN BY USING CONSUMER KEY AND REQUEST TOKEN
def get_access_token():

    logging.info("=== CONVERT YOUR REQUEST TOKEN INTO A POCKET ACCESS TOKEN ===")
    api.postAPI("https://getpocket.com/v3/oauth/authorize",
                         {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", "X-Accept": "application/json"},
                         {"consumer_key": "74406-8a08d271e96900d77476c4dc", "code": "d46f61c2-886b-ecbc-bc54-2d49a6"})


    d = json.loads(api.resp.text)
    for k in d.keys():
        logging.debug("%s:%s" %(k, d[k]))
    # return access token
    return d["access_token"]


if __name__ == "__main__":

    # rt = get_request_token()
    # logging.info("Request Token=%s" %(rt))


    at = get_access_token()
    logging.info("Access Token=%s" % (at))
