from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *



def all_service(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/all.png', _external=True),
            thumbnail_image_url='https://i.imgur.com/VTC5Vbq.png',
            title='請問想體驗哪項服務呢?',
            text='點選一個吧!',
            actions=[
                MessageAction(
                    label='餐點推薦',
                    text='想來點你推薦的餐點'
                ),
                MessageAction(
                    label='健身飲食提醒',
                    text='想知道一些小建議'
                ),
                MessageAction(
                    label='問題與解答',
                    text='幫我解惑一下吧'
                ),
                MessageAction(
                    label='其他補充',
                    text='想看看其他說明'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)



def recommend_choice(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/3pr2gMQ.png',
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
                    thumbnail_image_url='https://i.imgur.com/3pr2gMQ.png',
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
                            display_text='早餐當然要吃飽，推個450-600的食物!',
                            data='action=想來點推薦的料理&item=450-600'
                        )  
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/jA2pU6S.png',
                    title='隨機推薦',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        PostbackAction(
                            label='份量大',
                            display_text='想吃大份量的餐點!',
                            data='action=想來點推薦的料理&item=份量大'
                        ),
                        PostbackAction(
                            label='份量小',
                            display_text='想吃小份量的餐點!',
                            data='action=想來點推薦的料理&item=份量小'
                        ),
                        PostbackAction(
                            label='水果推薦',
                            display_text='水果推薦',
                            data='action=想來點推薦的料理&item=水果推薦'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)




def hint_service(event):
    message = TemplateSendMessage(
        alt_text='幫我解惑一下吧',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/u8uB9Jo.png',
                    title='問題集1',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='蛋白質吸收率是什麼？',
                            text='蛋白質吸收率是什麼？'
                        ),
                         MessageAction(
                            label='乳清蛋白真的有效嗎？',
                            text='乳清蛋白真的有效嗎？'
                        ),
                         MessageAction(
                            label='健身多快能看見成果？',
                            text='健身多快能看見成果？'
                        )

                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/u8uB9Jo.png',
                    title='問題集2',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='有段時間沒運動，身材會荒廢?',
                            text='有段時間沒運動，身材會荒廢'
                        ),
                         MessageAction(
                            label='吃點心都會覺得罪惡感高!',
                            text='吃點心都會覺得罪惡感高!'
                        ),
                         MessageAction(
                            label='吃外食還能維持好身材嗎？',
                            text='吃外食還能維持好身材嗎'
                        )  
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/O7Qh0jv.png',
                    title='問題集3-數值介紹',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='BMR-基礎代謝率',
                            text='基礎代謝率是什麼'
                        ),
                        MessageAction(
                            label='TDEE-每日總消耗熱量',
                            text='每日總消耗熱量是什麼'
                        ),
                        MessageAction(
                            label='改變的方法!',
                            text='改變代謝力'
                        )  
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def hint_service(event):
    message = TemplateSendMessage(
        alt_text='想知道一些小建議~',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/hint.png', _external=True),
            thumbnail_image_url='https://i.imgur.com/PfSTVkL.png',
            title='請問想知道哪項建議呢?',
            text='點選一個吧!',
            actions=[
                MessageAction(
                    label='增肌階段',
                    text='想知道有關增肌階段的建議'
                ),
                MessageAction(
                    label='減脂階段',
                    text='想看看有關減脂階段的建議'
                ),
                MessageAction(
                    label='休息階段',
                    text='來點休息期的建議吧'
                ),
                MessageAction(
                    label='其他建議',
                    text='看看其他建議有哪些'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def answer_service(event):
    message = TemplateSendMessage(
        alt_text='幫我解惑一下吧',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/u8uB9Jo.png',
                    title='問題集1',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='蛋白質吸收率是什麼？',
                            text='蛋白質吸收率是什麼？'
                        ),
                         MessageAction(
                            label='乳清蛋白真的有效嗎？',
                            text='乳清蛋白真的有效嗎？'
                        ),
                         MessageAction(
                            label='健身多快能看見成果？',
                            text='健身多快能看見成果？'
                        )

                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/u8uB9Jo.png',
                    title='問題集2',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='有段時間沒運動，身材會荒廢?',
                            text='有段時間沒運動，身材會荒廢'
                        ),
                         MessageAction(
                            label='吃點心都會覺得罪惡感高!',
                            text='吃點心都會覺得罪惡感高!'
                        ),
                         MessageAction(
                            label='吃外食還能維持好身材嗎？',
                            text='吃外食還能維持好身材嗎'
                        )  
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/O7Qh0jv.png',
                    title='問題集3-數值介紹',
                    text='想選多少熱量的餐點呢?',
                    actions=[
                        MessageAction(
                            label='BMR-基礎代謝率',
                            text='基礎代謝率是什麼'
                        ),
                        MessageAction(
                            label='TDEE-每日總消耗熱量',
                            text='每日總消耗熱量是什麼'
                        ),
                        MessageAction(
                            label='改變的方法!',
                            text='改變代謝力'
                        )  
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def other_service(event):
    message = TemplateSendMessage(
        alt_text='想看看其他說明',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='foodpng/other.png', _external=True),
            thumbnail_image_url='https://i.imgur.com/1TuMdxc.png',
            title='請問想看看哪項說明?',
            text='點選一個吧!',
            actions=[
                MessageAction(
                    label='自助餐',
                    text='跟我說有關挑選自助餐的事吧'
                ),
                MessageAction(
                    label='大餐',
                    text='想吃想吃，有甚麼該注意的'
                ),
                MessageAction(
                    label='水果',
                    text='有關水果，我該知道甚麼呢'
                ),
                    MessageAction(
                    label='飲料',
                    text=' 跟我說說選飲料的大學問!'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


service_or_not= TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='請問還需要其他服務嗎?',
            actions=[
                PostbackAction(
                    label='還需要服務',
                    display_text='還需要你的幫忙',
                    data='action=還需要'
                ),
                PostbackAction(
                    label='暫時先不用',
                    display_text='這樣就好，謝謝!',
                    data='action=暫時先不用'
                )
            ]
        )
    )

another_or_not= TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='要重選一次嗎?',
            actions=[
                PostbackAction(
                    label='再來一次吧!',
                    display_text='再給我一個當參考吧!',
                    data='action=再來一個吧'
                ),
                PostbackAction(
                    label='這個很好!',
                    display_text='這樣就好，謝謝!',
                    data='action=暫時先不用'
                )
            ]
        )
    )



