# -*- coding: utf-8 -*-
from ndm.exceptions import *


class AbstractTransport:
    """
    Abstraction for construct real transport
    """
    def __init__(self, *args, **kwargs):
        pass

    def send(self, recipient, title, message):
        """
        Sed notification to recipient
        :param str recipient: recipient ID for transport
        :param str title: title for message
        :param str message: short text message
        """
        raise AbstractMethodException('Abstract method not callable!')
