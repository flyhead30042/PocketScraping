from pocket_scraping.postman import WebAPI
import json
from pocket_scraping.__init__ import config, logging

GET_POCKET_DATA_URL = "https://getpocket.com/v3/get"
GET_POCKET_DATA_HEADER='{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8", "X-Accept": "application/json"}'



class PocketItem(object):
    def __init__(self, **kwargs):
        self.item_id = ""
        self.resolved_id = ""
        self.given_url = ""
        self.given_title = ""
        self.favorite = ""
        self.status = ""
        self.resolved_title = ""
        self.resolved_url = ""
        self.excerpt = ""
        self.is_article = ""
        self.has_image = ""
        self.has_video = ""
        self.word_count = ""


        for key in kwargs:
            # logging.debug("setting [%s]=%s" %(key, kwargs[key]))
            setattr(self, key, kwargs[key])

        self.images = []
        self.videos = []


class PocketImage(object):
    def __init__(self, **kwargs):
        self.item_id=""
        self.image_id=""
        self.src=""
        self.width=0
        self.height=0
        self.credit=""
        self.caption=""

        for key in kwargs:
            # logging.debug("setting [%s]=%s" %(key, kwargs[key]))
            setattr(self, key, kwargs[key])

class PocketVideo(object):
    def __init__(self, **kwargs):
        self.item_id=""
        self.video_id=""
        self.src=""
        self.width=0
        self.height=0
        self.type=0
        self.vid==""

        for key in kwargs:
            # logging.debug("setting [%s]=%s" %(key, kwargs[key]))
            setattr(self, key, kwargs[key])

def get_pocket_data(consumer_key, access_token, **kwargs):
    # logging.debug("additional params %s:" %(kwargs))
    postdata ={"consumer_key": consumer_key, "access_token": access_token}
    postdata.update(kwargs)
    # logging.debug("postdata %s:" %(postdata.items()))

    api = WebAPI()
    api.postAPI(url=config["GET_POCKET_DATA"]["GET_POCKET_DATA_URL"],
                headers=json.loads(config["GET_POCKET_DATA"]["GET_POCKET_DATA_HEADER"]),
                postdata=postdata
               )

    plist = json.loads(api.resp.text)["list"]

    pdata=[]
    for id in plist:
        d = plist[id]
        pitem = PocketItem(**d)
        # logging.debug("Item(%s)%s" %(pitem.item_id, pitem.given_title))

        if pitem.has_image == "1":
            for id in d["images"]:
                logging.debug("Image(%s)%s" %(id, d["images"][id]))
                pimage = PocketImage(**d["images"][id])
                pitem.images.append(pimage)

        if pitem.has_video == "1":
            for id in d["videos"]:
                logging.debug("Video(%s)%s" %(id, d["videos"][id]))
                pvideo = PocketVideo(**d["videos"][id])
                pitem.videos.append(pvideo)

        pdata.append(pitem)
        logging.debug("Item(%s)%s" %(pitem.item_id, pitem.given_title))

    return pdata

