from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *



def encouragment_templet():
    msg=[]
    msg.append(TextSendMessage(text='嗨哈囉'))
    print('msg from [', user_name, '](', user_id, ') : ', msg) #修改
    buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/w1JM4f5.jpg',
            title='問心情',
            text='最近練得怎麼樣啊？心情還行ㄇ？',
            actions=[PostbackAction(
                    label='我不好',
                    display_text='心情不好，健身好挫折qq'
                    ),
                    MessageAction(
                    label='心情還行',
                    text='心情普通，但想要更開心一點'
                    ),
                    MessageAction(
                    label='心情很好',
                    text='我現在心情很好der la～'
                    )
                ]
            )
        )
    line_bot_api.reply_message(event.reply_token, buttons_template_message)


