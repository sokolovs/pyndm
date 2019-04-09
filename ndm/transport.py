# -*- coding: utf-8 -*-
from ndm.exceptions import *


class AbstractTransport(object):
    """
    Abstraction for construct real transport
    """
    def __init__(self, *args, **kwargs):
        pass

    def send(self, recepient, title, message):
        """
        Sed notification to recepient
        :param str recepient: recepient ID for transport
        :param str title: title for message
        :param str message: short text message
        """
        raise AbstractMethodException('Abstract method not callable!')
