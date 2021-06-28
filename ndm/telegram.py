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
    read_timeout = 30  # read data timeout, sec

    def __init__(
            self, api_key, api_url=None, conn_timeout=None, read_timeout=None):
        """
        Create telegram transport instance
        :param str api_key: telegram bot API key
        :param str api_url: (optional) base API URL
        :param int conn_timeout: (optional) connection timeout
        :param int read_timeout: (optional) response read timeout
        """
        self.api_key = api_key
        if api_url:
            self.api_url = api_url
        if conn_timeout and isinstance(conn_timeout, int):
            self.conn_timeout = conn_timeout
        if read_timeout and isinstance(read_timeout, int):
            self.read_timeout = read_timeout

    def send(self, recipient, title, message):
        """
        Send notification to recipient
        :param str recipient: message recipient ID (Telegram chat ID)
        :param str title: title for message
        :param str message: short text message
        :raise TelegramAPIException: telegram API exception
        """
        rdata = None
        url = '%s/bot%s/sendMessage' % (self.api_url, self.api_key)
        data = {
            'parse_mode': 'HTML',
            'chat_id': recipient,
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
