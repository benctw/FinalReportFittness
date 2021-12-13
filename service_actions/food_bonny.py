from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *


def all_service(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='foodpng/7all.png', _external=True),
            thumbnail_image_url='https://i.imgur.com/oERO00m.png',
            title='請問想體驗哪項服務呢?',
            text='點選一個吧!',
            actions=[
                MessageAction(
                    label='餐點推薦',
                    text='想來點推薦的料理'
                ),
                MessageAction(
                    label='健身飲食提醒',
                    text='想知道一些小建議~'
                ),
                MessageAction(
                    label='問題與解答',
                    text='幫我解惑'
                ),
                MessageAction(
                    label='其他補充',
                    text='想看看其他說明'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)



def other_choice(event):
    message = TemplateSendMessage(
        alt_text='想來點推薦的料理',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/ZvZAhx',
                    title='正餐推薦',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        PostbackAction(
                            label='0-300',
                            display_text='想吃0-300大卡的餐點，來點推薦吧!',
                            data='action=想來點推薦的料理&item=0-300'
                        ),
                         PostbackAction(
                            label='300-550',
                            display_text='給我個300-550的餐點吧!',
                            data='action=想來點推薦的料理&item=300-550'
                        ),
                         PostbackAction(
                            label='550-800',
                            display_text='胃口大開，550-800的來一份!',
                            data='action=想來點推薦的料理&item=550-800'
                        )

                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/ZvZAhx',
                    title='早餐推薦',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        PostbackAction(
                            label='0-250',
                            display_text='想吃0-250大卡的餐點，來點推薦吧!',
                            data='action=想來點推薦的料理&item=0-250'
                        ),
                         PostbackAction(
                            label='250-450',
                            display_text='給我個250-450的餐點吧!',
                            data='action=想來點推薦的料理&item=250-450'
                        ),
                         PostbackAction(
                            label='450-600',
                            display_text='胃口大開，550-800的來一份!',
                            data='action=想來點推薦的料理&item=450-600'
                        )  
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/cFDsIi',
                    title='隨機推薦',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        PostbackAction(
                            label='份量大',
                            display_text='想吃小份量的餐點!',
                            data='action=想來點推薦的料理&item=份量大'
                        ),
                         PostbackAction(
                            label='份量小',
                            display_text='想吃小份量的餐點!',
                            data='action=想來點推薦的料理&item=份量小'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

