# -*- coding: utf-8 -*-
import logging

from ndm.exceptions import SendSMSException
from ndm.transport import AbstractTransport

import smpplib.client
import smpplib.consts
import smpplib.gsm

logging.basicConfig(level='INFO')


class SMS(AbstractTransport):
    """ SMS SMPP transport """
    name = 'SMS'
    timeout = 5

    def __init__(self, source, host='localhost', port=2775, auth_pair=None):
        """
        Create SMPP transport instance
        :param str source: sender phone or string ID
        :param str host: hostname or IP for SMPP server
        :param int port: TCP port for SMPP server
        :param tuple auth_pair: login and password
        """
        self.source = source
        self.host = host
        self.port = port
        self.auth_pair = auth_pair
        self.login = None
        self.passwd = None
        if auth_pair:
            self.login, self.passwd = auth_pair

    def send(self, recipient, title, message):
        """
        Send notification to recipient
        :param str recipient: phone number
        :param str title: title for message (including in SMS)
        :param str message: short text message
        """
        # Replace bad symbols in phone
        for char in '+()- ':
            recipient = recipient.replace(char, '')

        # Convert to unicode
        if type(title) != str:
            title = title.decode('utf-8')
        if type(message) != str:
            message = message.decode('utf-8')

        client = None
        if title:
            text = '%s:\n%s' % (title, message)
        else:
            text = message
        parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(text)
        try:
            client = smpplib.client.Client(self.host, self.port)
            client.connect()
            if self.auth_pair:
                client.bind_transceiver(
                    system_id=self.login,
                    password=self.passwd)
            for part in parts:
                client.send_message(
                    source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
                    source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
                    source_addr=self.source,
                    dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
                    dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
                    destination_addr=recipient,
                    short_message=part,
                    data_coding=encoding_flag,
                    esm_class=msg_type_flag
                )
        except Exception as e:
            raise SendSMSException(e)
        finally:
            if client:
                try:
                    client.unbind()
                except:
                    pass
                client.disconnect()
        return False
