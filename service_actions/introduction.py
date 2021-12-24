from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *


def call_introduction(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
                    title='請問想要知道什麼設施的介紹呢?',
                    text='請在下方點選您想知道的項目',
                    actions=[
                        MessageAction(
                        label='臥姿彎腿機',
                        display_text='我想知道臥姿彎腿機怎麼用'
                        ),
                        MessageAction(
                        label='背伸機',
                        display_text='我想知道背伸機怎麼用'
                        ),
                        MessageAction(
                        label='大腿推蹬機',
                        display_text='我想知道大腿推蹬機怎麼用'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
                    title='請問想要知道什麼設施的介紹呢?',
                    text='請在下方點選您想知道的項目',
                    actions=[
                        MessageAction(
                        label='腿內收機',
                        display_text='我想知道腿內收機怎麼用'
                        ),
                        MessageAction(
                        label='腿外展機',
                        display_text='我想知道腿外展機怎麼用'
                        ),
                        MessageAction(
                        label='腿部伸張機',
                        display_text='我想知道腿部伸張機怎麼用'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
                    title='請問想要知道什麼設施的介紹呢?',
                    text='請在下方點選您想知道的項目',
                    actions=[
                        MessageAction(
                        label='腹部旋轉機',
                        display_text='我想知道腹部旋轉機怎麼用'
                        ),
                        MessageAction(
                        label='二頭訓練機',
                        display_text='我想知道二頭訓練機怎麼用'
                        ),
                        MessageAction(
                        label='三頭訓練機',
                        display_text='我想知道三頭訓練機怎麼用'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)