from flask import Flask, request, abort, url_for
from linebot.models import events
from line_chatbot_api import *

def call_BMI(event):
    messages = []
    messages.append(TextSendMessage(text='請分別輸入身高(cm)和體重(kg)並用空格隔開'))
    
    line_bot_api.reply_message(event.reply_token, messages)

def calculate_BMI(event,recrive_text):
    message = []
    
    try:
        height, weight = recrive_text.split()
        height = float(height)  # cm
        weight = float(weight)  # kg

        BMI = weight/(height/100)**2

        message.append(TextSendMessage(text='你的BMI為{:.1f}'.format(BMI)))
        
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "小幫手目前沒有這個功能哦~"))
    
    if BMI >= 24:
        message.append(TextMessage(text='你的體重過重了，建議多多運動'))
        message.append(StickerSendMessage(package_id=6362, sticker_id=11087933))
    elif 18.5 <= BMI <24:
        message.append(TextSendMessage(text='你的BMI界於正常範圍，繼續保持'))
        message.append(StickerSendMessage(package_id=11537, sticker_id=52002734))
    else:
        message.append(TextSendMessage(text='你的體重過輕了，建議多吃一點'))
        message.append(StickerSendMessage(package_id=1070, sticker_id=17847))

    line_bot_api.reply_message(event.reply_token,message)