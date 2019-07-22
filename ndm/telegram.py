# -*- coding: utf-8 -*-
from ndm.exceptions import TelegramAPIException
from ndm.transport import AbstractTransport

import requests

# import logging
# logging.basicConfig(level='DEBUG')


class Telegram(AbstractTransport):
    """ Telegram transport """
    name = 'Telegram'
    api_url = 'https://api.telegram.org'
    conn_timeout = 3   # connection timeout, sec
    read_timeout = 10  # read data timeout, sec

    def __init__(self, api_key, api_url=None):
        """
        Create telegram transport instance
        :param str api_key: telegram bot API key
        :param str api_url: (optional) base API URL
        """
        self.api_key = api_key
        if api_url:
            self.api_url = api_url

    def send(self, recepient, title, message):
        """
        Send notification to recepient
        :param str recepient: message recepient ID (Telegram chat ID)
        :param str title: title for message
        :param str message: short text message
        :raise TelegramAPIException: telegram API exception
        """
        rdata = None
        url = '%s/bot%s/sendMessage' % (self.api_url, self.api_key)
        data = {
            'parse_mode': 'HTML',
            'chat_id': recepient,
            'text': '<b>%s</b>:\n%s' % (title, message)
        }
        response = requests.post(
            url=url, data=data, timeout=(self.conn_timeout, self.read_timeout))
        if response.ok:
            rdata = response.json()
            if 'ok' in rdata.keys() and rdata['ok']:
                return True
        else:
            try:
                rdata = response.json()
            except:
                pass
            if rdata and 'ok' in rdata.keys() and not rdata['ok']:
                if 'description' in rdata.keys():
                    raise TelegramAPIException(rdata['description'])
        return False
