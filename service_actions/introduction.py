from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *

def call_service(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
            title='請問想要知道什麼設施的介紹呢?',
            text='請在下方點選您想知道的項目',
            actions=[
                MessageAction(
                    label='跑步機',
                    text='我想知道跑步機怎麼用'
                ),
                MessageAction(
                    label='滑步機',
                    text='我想知道滑步機怎麼用'
                ),
                MessageAction(
                    label='划船機',
                    text='我想知道划船機怎麼用'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)