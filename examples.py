from ndm import *

# Telegram transport
tlg = Telegram(api_key='648160995:AaG40neCoWX8BB6V7Wh1ELK-uR4pdgTTWxX')
# tlg = Telegram(
#     api_key='648160995:AaG40neCoWX8BB6V7Wh1ELK-uR4pdgTTWxX',
#     api_url='http://proxy-addr.net:18080')
tlg.send('183327952', 'Title', 'Message')

# Email transport
email = Email(
    from_email='mybox@mail.com',
    host='smtp.mail.com',
    port=465,
    auth_pair=('mybox@mail.com', 'mypass'),
    secure=True
)
# For send from localhost without password
# email = Email(from_email='mybox@mail.com')
email.send('other@mail.com', 'Subject', 'Message')

# SMS transport
sms = SMS(
    source='PhoneOrName',
    host='bsms-proxy.tele2.ru',
    port=2775,
    auth_pair=('smpp_system_id', 'password')
)
# Title and message will be concatenate with ':' and newline
sms.send('79407775544', 'Title', 'Message')
# Without title
sms.send('79407775544', False, 'Message')
