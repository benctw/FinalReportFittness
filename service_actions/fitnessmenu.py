from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *


def call_fitnessmeun(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
                    title='健身菜單推薦',
                    text='選擇適合自己課程',
                    actions=[
                         MessageAction(
                        label='健身小常識',
                        text='健身小常識'
                        ),
                         MessageAction(
                        label='菜單攻略',
                        text='菜單攻略'
                        ),
                        MessageAction(
                        label='初級菜單',
                        text='初級菜單'
                        ),
                        MessageAction(
                        label='進階菜單',
                        text='進階菜單'
                        ),
                        
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/rfgMcFM.jpg',
                    title='徒手健身',
                    text='徒手健身',
                    actions=[
                         MessageAction(
                        label='徒手健身介紹',
                        text='徒手健身介紹'
                        ),
                         MessageAction(
                        label='徒手健身day1',
                        text='徒手健身day1'
                        ),
                        MessageAction(
                        label='徒手健身day2',
                        text='徒手健身day2'
                        ),
                        MessageAction(
                        label='徒手健身day3',
                        text='徒手健身day3'
                        ),
                        MessageAction(
                        label='徒手健身day4',
                        text='徒手健身day4'
                        )   
                        MessageAction(
                        label='徒手健身day5',
                        text='徒手健身day5'
                        )   
                        MessageAction(
                        label='徒手健身day6',
                        text='徒手健身day6'
                        )   
                        MessageAction(
                        label='徒手健身day7',
                        text='徒手健身day7'
                        )   
                  
                
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)