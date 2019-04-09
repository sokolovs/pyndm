# -*- coding: utf-8 -*-
import requests
from ndm.transport import AbstractTransport


class Telegram(AbstractTransport):
    name = 'Telegram'
    api_url = 'https://api.telegram.org'
    conn_timeout = 3  # connection timeout, sec
    read_timeout = 10 # read data timeout, sec

    def __init__(self, api_key):
        self.api_key = api_key

    def send(self, recepient, title, message):
        """
        Sed notification to recepient
        :param str recepient: recepient ID for transport
        :param str title: title for message
        :param str message: short text message
        """
        url = '%s/bot%s/sendMessage' % (self.api_url, self.api_key)
        data = 'parse_mode=HTML&chat_id=%s&text=<b>%s</b>:+%s' % \
            (recepient, title, message)
        response = requests.post(url=url, data=data,
            timeout=(self.conn_timeout, self.read_timeout)
        )
