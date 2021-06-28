# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ndm.exceptions import SendMailException
from ndm.transport import AbstractTransport

# import logging
# logging.basicConfig(level='DEBUG')


class Email(AbstractTransport):
    """ Email transport """
    name = 'Email'
    timeout = 5

    def __init__(
            self, from_email, host='localhost', port=25,
            auth_pair=None, secure=False):
        """
        Create email transport instance
        :param str from_email: sender email
        :param str host: hostname or IP for SMTP server
        :param int port: TCP port for SMTP server
        :param tuple auth_pair: login and password
        :param bool secure: create secure SMTP connection or not
        """
        self.from_email = from_email
        self.host = host
        self.port = port
        self.auth_pair = auth_pair
        self.login = None
        self.passwd = None
        if auth_pair:
            self.login, self.passwd = auth_pair
        self.secure = secure

    def send(self, recipient, title, message):
        """
        Send notification to recipient
        :param str recipient: message recipient ID (email or
            comma-separated list of email)
        :param str title: email subject
        :param str message: email text
        :raise SendMailException: send exception
        """
        # Convert to unicode
        if type(title) != str:
            title = title.decode('utf-8')
        if type(message) != str:
            message = message.decode('utf-8')

        server = None
        try:
            # Create and configure server instance
            mksrv = smtplib.SMTP_SSL if self.secure else smtplib.SMTP
            server = mksrv(self.host, self.port, timeout=self.timeout)
            if self.auth_pair:
                server.login(self.login, self.passwd)

            # Create mime message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = title
            msg['From'] = self.from_email
            msg['To'] = recipient

            # Create mime parts
            text_part = MIMEText(message, 'plain', 'utf-8')
            html_part = MIMEText(
                '<p><b>%s:</b><br/>%s</p>' %
                (title, message), 'html', 'utf-8')
            msg.attach(text_part)
            msg.attach(html_part)

            # Send
            server.sendmail(self.from_email, recipient, msg.as_string())
            return True
        except Exception as e:
            raise SendMailException(e)
        finally:
            if server:
                server.quit()
        return False
