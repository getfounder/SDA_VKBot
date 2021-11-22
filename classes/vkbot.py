import config as cfg

from functions import *

from time import sleep

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id


class VKBot:
    def __init__(self, token):
        """
        ------------------------------------------------------------------------------------------
        Initialization. Connection via API. Search for working sessions.

        type(token) >> str
        ------------------------------------------------------------------------------------------
        """

        self.connect = vk_api.VkApi(token=token)
        self.session = self.connect.get_api()
        self.upload = VkUpload(self.session)

        return "VKBot has been started"

    def upload_photo(self, path_photo):
        """
        ------------------------------------------------------------------------------------------
        Uploading photos to VK for further sending.

        type(path_photo) >> str
        ------------------------------------------------------------------------------------------
        """

        response = self.upload.photo_messages(path_photo)[0]

        owner_id = response['owner_id']
        photo_id = response['id']
        access_key = response['access_key']

        return owner_id, photo_id, access_key

    def send_img(self, peer_id, path_photo):
        """
        ------------------------------------------------------------------------------------------
        Sending a message in vk.

        type(peer_id) >> int
        type(photo) >> str
        ------------------------------------------------------------------------------------------
        """
        owner_id, photo_id, access_key = self.upload_photo(path_photo)
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'

        self.session.messages.send(
            random_id=get_random_id(),
            peer_id=peer_id,
            attachment=attachment
        )
        return "Image has been sent"
        
    def start(self):
        result = None
        longpool = VkLongPoll(self.connect)
        for event in longpool.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    id = event.user_id
                    # make_screenshot(cfg.bbox["SG_code"], cfg.filenames["SG_code"])
                    result = self.send_img(id, f"screens/{cfg.filenames['SG_code']}")

        sleep(0.025)
        return result