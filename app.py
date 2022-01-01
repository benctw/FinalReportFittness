# import flask related
import re
from flask import Flask, request, abort, url_for, render_template
from urllib.parse import parse_qsl, parse_qs
import random,os, json, sqlite3
from linebot.models import events
from line_chatbot_api import *
from service_actions.BMI import *
from service_actions.introduction import *
from service_actions.food_bonny import *
from service_actions.allfoodlist import *
from service_actions.encouragment import *
from access_sqlite_db import *
#import picture related
from array import array
import os, time
from PIL import Image
import sys
import time
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# create flask server
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

# handle msg
import os
# import speech_recognition as sr

def transcribe(wav_path):
    '''
    Speech to Text by Google free API
    language: en-US, zh-TW
    '''
    
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio, language="zh-TW")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

@handler.add(PostbackEvent)
def handle_postback(event):
    line_user_name = line_bot_api.get_profile(event.source.user_id).display_name
    line_user_id = event.source.user_id
    user_data = read_user_data(line_user_id, line_user_name)
    user_age=user_data[4] if user_data[4] else 0
    user_kg=user_data[2] if user_data[2] else 0
    user_cm=user_data[3] if user_data[3] else 0
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    # print(postback_data.get('action', ''))
    # print(postback_data.get('item', ''))
    sticker_list=[(1070, 17839), (6362, 11087920), (11537, 52002734), (8525, 16581293),(8522,16581266),(446,1997),(6362,11087932)]
    if postback_data.get('action')=='想來點推薦的料理':
        if postback_data.get('item')=='0-300':
            random_number = random.randint(0,len(food_diet1)-1)
            messages=[]
            # print(random_number)
            # print(food_diet1[random_number])
            messages.append(StickerSendMessage(package_id=446, sticker_id=1997))
            messages.append(TextSendMessage(text=f'推薦你吃{food_diet1[random_number][0]}，熱量大約{food_diet1[random_number][1]}大卡'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='300-550':
            random_number = random.randint(0,len(food_diet2)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1997))
            messages.append(TextSendMessage(text=f'熱量{food_diet2[random_number][1]}大卡的{food_diet2[random_number][0]}，推薦給你參考!'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='550-800':
            random_number = random.randint(0,len(food_diet3)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1997))
            messages.append(TextSendMessage(text=f'推薦你吃{food_diet3[random_number][0]}，熱量大約{food_diet3[random_number][1]}大卡'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)


        elif postback_data.get('item')=='0-250':
            random_number = random.randint(0,len(food_breakfast1)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=6362, sticker_id=11087932))
            messages.append(TextSendMessage(text=f'熱量{food_breakfast1[random_number][1]}大卡的{food_breakfast1[random_number][0]}，推薦給你參考!'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='250-450':
            random_number = random.randint(0,len(food_breakfast2)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=6362, sticker_id=11087932))
            messages.append(TextSendMessage(text=f'推薦你吃{food_breakfast2[random_number][0]}，熱量大約{food_breakfast2[random_number][1]}大卡'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='450-600':
            random_number = random.randint(0,len(food_breakfast3)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=6362, sticker_id=11087932))
            messages.append(TextSendMessage(text=f'熱量{food_breakfast3[random_number][1]}大卡的{food_breakfast3[random_number][0]}，推薦給你參考!'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        
        elif postback_data.get('item')=='份量大':
            random_number = random.randint(0,len(food_big)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1997))
            messages.append(TextSendMessage(text=f'我覺得{food_big[random_number]}是個不錯的選擇!'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='份量小':
            random_number = random.randint(0,len(food_small)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=6362, sticker_id=11087932))
            messages.append(TextSendMessage(text=f'可以試試看{food_small[random_number]}'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif postback_data.get('item')=='水果推薦':
            random_number = random.randint(0,len(food_fruit)-1)
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1997))
            messages.append(TextSendMessage(text=f'吃{food_fruit[random_number]}吧，剛好是一份的量!'))
            messages.append(another_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
    elif postback_data.get('action')=='再一次食物服務':
        food_service(event, user_data) 
    elif postback_data.get('action')=='再來一個吧':
        recommend_choice(event)  
    elif postback_data.get('action')=='先不用喔!':
        messages=[]
        messages.append(StickerSendMessage(package_id=8522, sticker_id=16581266))
        messages.append(TextSendMessage(text='不用客氣，很高興為您服務!'))
        line_bot_api.reply_message(event.reply_token, messages)


######################以下兩個未知#################################
    elif postback_data.get('action')=='還需要其他介紹':
        call_introduction(event)  
    elif postback_data.get('action')=='暫時先不用其他介紹':
        messages=[]
        messages.append(StickerSendMessage(package_id=11537, sticker_id=52002734))
        messages.append(TextSendMessage(text='祝您有愉快的健身體驗'))
        line_bot_api.reply_message(event.reply_token, messages)
#####################################################################


@handler.add(MessageEvent)
def handle_something(event):
    line_user_name = line_bot_api.get_profile(event.source.user_id).display_name
    line_user_id = event.source.user_id
    user_data = read_user_data(line_user_id, line_user_name)
    user_age=user_data[4] if user_data[4] else 0
    user_kg=user_data[2] if user_data[2] else 0
    user_cm=user_data[3] if user_data[3] else 0
    function_handle_something(event, user_data)

    if event.message.type=='text':
        recrive_text=event.message.text
        # print(recrive_text)#098
        if '器材操作說明' in recrive_text:
            # print(url_for('static', filename='images/brown_1024.jpg', _external=True))
            call_introduction(event)
        elif '我想知道臥姿彎腿機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://www.gofitness.fi/images/products/screen-shot-2020-11-16-at-110018_orig.png', preview_image_url='https://www.gofitness.fi/images/products/screen-shot-2020-11-16-at-110018_orig.png'))
            messages.append(TextSendMessage(text='臥姿彎腿機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)  
        elif '我想知道背伸機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://f1-recreation.com.tw/images/com_hikashop/upload/202.jpg', preview_image_url='https://f1-recreation.com.tw/images/com_hikashop/upload/202.jpg'))
            messages.append(TextSendMessage(text='背伸機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages) 
        elif '我想知道大腿推蹬機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://gracegodfitness.com/wp-content/uploads/2019/08/DF201-%E5%A4%A7%E8%85%BF%E6%8E%A8%E8%B9%AC%E5%B0%8F%E8%85%BF%E4%BC%B8%E5%BC%B5%E8%A8%93%E7%B7%B4%E6%A9%9F-.jpg', preview_image_url='https://gracegodfitness.com/wp-content/uploads/2019/08/DF201-%E5%A4%A7%E8%85%BF%E6%8E%A8%E8%B9%AC%E5%B0%8F%E8%85%BF%E4%BC%B8%E5%BC%B5%E8%A8%93%E7%B7%B4%E6%A9%9F-.jpg'))
            messages.append(TextSendMessage(text='大腿推蹬機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道腿內收機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://www.ruizhong.com.tw/images/products/Leg-retractor-N952.jpg', preview_image_url='https://www.ruizhong.com.tw/images/products/Leg-retractor-N952.jpg'))#ori
            messages.append(TextSendMessage(text='腿內收機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道腿外展機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://www.f1-recreation.com.tw/images/com_hikashop/upload/ss-hab.jpg', preview_image_url='https://www.f1-recreation.com.tw/images/com_hikashop/upload/ss-hab.jpg'))
            messages.append(TextSendMessage(text='腿外展機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道三頭訓練機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://f1-recreation.com.tw/images/com_hikashop/upload/ss-tp.jpg', preview_image_url='https://f1-recreation.com.tw/images/com_hikashop/upload/ss-tp.jpg'))
            messages.append(TextSendMessage(text='三頭訓練機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道腹部旋轉機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://www.moonskyedu.com/bodybuild/%E8%B3%87%E6%96%99%E5%9C%96%E7%89%87/%E5%81%A5%E8%BA%AB%E5%99%A8%E6%9D%90/%E8%85%B9%E6%97%8B%E8%BD%89%E6%A9%9F1.jpg', preview_image_url='https://www.moonskyedu.com/bodybuild/%E8%B3%87%E6%96%99%E5%9C%96%E7%89%87/%E5%81%A5%E8%BA%AB%E5%99%A8%E6%9D%90/%E8%85%B9%E6%97%8B%E8%BD%89%E6%A9%9F1.jpg'))
            messages.append(TextSendMessage(text='腹部旋轉機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道二頭訓練機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://gracegodfitness.com/wp-content/uploads/2019/08/S912-%E8%82%B1%E4%BA%8C%E9%A0%AD%E8%82%8C%E5%BD%8E%E6%9B%B2%E6%A9%9F.png', preview_image_url='https://gracegodfitness.com/wp-content/uploads/2019/08/S912-%E8%82%B1%E4%BA%8C%E9%A0%AD%E8%82%8C%E5%BD%8E%E6%9B%B2%E6%A9%9F.png'))
            messages.append(TextSendMessage(text='二頭訓練機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我想知道腿部伸張機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://www.gosportsart.com/wp-content/uploads/2020/04/N957-web-2048x1366.jpg', preview_image_url='https://www.gosportsart.com/wp-content/uploads/2020/04/N957-web-2048x1366.jpg'))
            messages.append(TextSendMessage(text='腿部伸張機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif '飲食推薦' in recrive_text:
            food_service(event, user_data)
        elif '想來點你推薦的餐點' in recrive_text:
            recommend_choice(event)
        elif '想知道一些小建議' in recrive_text:
            hint_service(event)
        elif '幫我解惑一下吧' in recrive_text:
            answer_service(event)
        elif '想看看其他說明' in recrive_text:
            other_service(event)
        elif '設定體重' == recrive_text:
            update_user_action(line_user_id, 'set_kg')
            message = TextSendMessage(text='請輸入您的體重(公斤)')
            line_bot_api.reply_message(event.reply_token, message)
        elif '設定身高' == recrive_text:
            update_user_action(line_user_id, 'set_cm')
            message = TextSendMessage(text='請輸入您的身高(公分)')
            line_bot_api.reply_message(event.reply_token, message)
        elif '設定年紀' == recrive_text:
            update_user_action(line_user_id, 'set_age')
            message = TextSendMessage(text='請輸入您的年紀(歲)')
            line_bot_api.reply_message(event.reply_token, message)

        elif '好啊!我是男生' == recrive_text:
            if user_kg and user_cm and user_age:
                message = TextSendMessage(text=f'BMR為{(13.7*user_kg)+(5.0*user_cm)-(6.8*user_age)+66:.1f}')
                line_bot_api.reply_message(event.reply_token, message)
            else:
                message = TextSendMessage(text='請記得先設定身高, 體重, 年紀喔~',quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=MessageAction(label=f"體重{user_kg}公斤" if user_kg else "體重未設定", text="設定體重")),
                                                QuickReplyButton(action=MessageAction(label=f"身高{user_cm}公分" if user_cm else "身高未設定", text="設定身高")),
                                                QuickReplyButton(action=MessageAction(label=f"年紀{user_age}歲" if user_age else "年紀未設定", text="設定年紀"))
                                                ]))
                line_bot_api.reply_message(event.reply_token, message)

        elif '好啊!我是女生' == recrive_text:
            if user_kg and user_cm and user_age:
                message = TextSendMessage(text=f'BMR為{(9.6*user_kg)+(1.8*user_cm)-(4.7*user_age)+655:.1f}')
                line_bot_api.reply_message(event.reply_token, message)
            else:
                message = TextSendMessage(text='請記得先設定身高, 體重, 年紀喔~',quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=MessageAction(label=f"體重{user_kg}公斤" if user_kg else "體重未設定", text="設定體重")),
                                                QuickReplyButton(action=MessageAction(label=f"身高{user_cm}公分" if user_cm else "身高未設定", text="設定身高")),
                                                QuickReplyButton(action=MessageAction(label=f"年紀{user_age}歲" if user_age else "年紀未設定", text="設定年紀"))
                                                ]))
                line_bot_api.reply_message(event.reply_token, message)

        elif read_user_action(line_user_id):
            user_action = read_user_action(line_user_id)
            if user_action == 'set_kg':
                if recrive_text.isnumeric():
                    update_user_kg(line_user_id, recrive_text)
                    update_user_action(line_user_id, '')
                    user_data = read_user_data(line_user_id, line_user_name)
                    user_kg = user_data[2] if user_data[2] else None
                    user_cm = user_data[3] if user_data[3] else None
                    user_age = user_data[4] if user_data[4] else None
                    message = TextSendMessage(text='體重設定成功',
                                            quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=MessageAction(label=f"體重{user_kg}公斤" if user_kg else "體重未設定", text="設定體重")),
                                                QuickReplyButton(action=MessageAction(label=f"身高{user_cm}公分" if user_cm else "身高未設定", text="設定身高")),
                                                QuickReplyButton(action=MessageAction(label=f"年紀{user_age}歲" if user_age else "年紀未設定", text="設定年紀"))
                                                ]))
                else:
                    message = TextSendMessage(text='請輸入數字')
                line_bot_api.reply_message(event.reply_token, message)
            elif user_action == 'set_cm':
                if recrive_text.isnumeric():
                    update_user_cm(line_user_id, recrive_text)
                    update_user_action(line_user_id, '')
                    user_data = read_user_data(line_user_id, line_user_name)
                    user_kg = user_data[2] if user_data[2] else None
                    user_cm = user_data[3] if user_data[3] else None
                    user_age = user_data[4] if user_data[4] else None
                    message = TextSendMessage(text='身高設定成功',
                                            quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=MessageAction(label=f"體重{user_kg}公斤" if user_kg else "體重未設定", text="設定體重")),
                                                QuickReplyButton(action=MessageAction(label=f"身高{user_cm}公分" if user_cm else "身高未設定", text="設定身高")),
                                                QuickReplyButton(action=MessageAction(label=f"年紀{user_age}歲" if user_age else "年紀未設定", text="設定年紀"))
                                                ]))
                else:
                    message = TextSendMessage(text='請輸入數字')
                line_bot_api.reply_message(event.reply_token, message)
            elif user_action == 'set_age':
                if recrive_text.isnumeric():
                    update_user_age(line_user_id, recrive_text)
                    update_user_action(line_user_id, '')
                    user_data = read_user_data(line_user_id, line_user_name)
                    user_kg = user_data[2] if user_data[2] else None
                    user_cm = user_data[3] if user_data[3] else None
                    user_age = user_data[4] if user_data[4] else None
                    message = TextSendMessage(text='年紀設定成功',
                                            quick_reply=QuickReply(items=[
                                                QuickReplyButton(action=MessageAction(label=f"體重{user_kg}公斤" if user_kg else "體重未設定", text="設定體重")),
                                                QuickReplyButton(action=MessageAction(label=f"身高{user_cm}公分" if user_cm else "身高未設定", text="設定身高")),
                                                QuickReplyButton(action=MessageAction(label=f"年紀{user_age}歲" if user_age else "年紀未設定", text="設定年紀"))
                                                ]))
                else:
                    message = TextSendMessage(text='請輸入數字')
                line_bot_api.reply_message(event.reply_token, message)
        

        elif '想知道有關增肌階段的建議' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='高碳水化合物\n體重*0.45*2=所需碳水\n碳水40-50%,蛋白質30-40%,脂肪10-30%'))
            messages.append(TextSendMessage(text='澱粉：五穀米、糙米、藜麥、燕麥片\n蛋白質：優格、牛奶、無糖豆漿、雞蛋、鮭魚、火雞肉等；\n健康脂肪：橄欖油、堅果\n綜合蔬果：高麗菜、空心菜、奇異果、芭樂'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '想看看有關減脂階段的建議' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='低碳水化合物\n體重*0.45*0.75=所需碳水化合物\n體重*0.45*1.5=所需蛋白質\n蛋白質40-50%,碳水20-30%,脂肪20-40%'))
            messages.append(TextSendMessage(text='澱粉：紫米飯、南瓜、馬鈴薯\n蛋白質：魚肉、瘦肉、藜麥、乳清蛋白\n優質脂肪類：含Omega-3,Omega-6的植物油\n綜合蔬果：沙拉、花椰菜、香蕉、莓果'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '來點休息期的建議吧' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='(天然、低脂、低糖食)，以下僅參考\n蛋白質40-50%,碳水20-30%,脂肪20-40%'))
            messages.append(TextSendMessage(text='澱粉：地瓜、五穀米\n蛋白質：毛豆、豆腐、雞腿、海鮮\n不飽和脂肪酸：酪梨'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '看看其他建議有哪些' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='1. 減少每天攝取的熱量\n2. 每天減少250大卡，增加運動消耗250大卡\n3. 吃原態食物避免加工食品'))
            messages.append(TextSendMessage(text='4. 吃複合式碳水，如蔬菜水果、豆類、全穀物\n5. 有氧運動和無氧的肌力訓練都很重要'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '蛋白質吸收率是什麼？' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='指食物蛋白質在消化道內被分解和吸收的程度，而通常植物性比動物性食物的蛋白消化率低。'))
            messages.append(TextSendMessage(text='一般烹調的消化率為：奶類97%～98%，肉類92%～94%，蛋類98%，大米82%，米飯及面製品為80%左右，土豆74%。'))
            messages.append(TextSendMessage(text='但纖維素經軟化破壞或除去後，植物蛋白的消化率可以提高。如大豆蛋白的消化率為60%，加工成豆腐及其它豆製品後，可提高到92%～100%。'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '乳清蛋白真的有效嗎？' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='簡介：\n提供人體所需的胺基酸和蛋白質，是幫助人體生長、發育、抗衰老的優質蛋白質。較易被消化吸收，含有多種免疫球蛋白及其他活性成分，脂肪及乳糖含量低。'))
            messages.append(TextSendMessage(text='好處：\n1.提高基礎代謝率，幫助燃脂效率\n2.降血壓、降血糖、降血脂改善胰島素敏感度\n3.降低身體的發炎指數\n4.增加飽足感，減少飢餓'))
            messages.append(TextSendMessage(text='食用注意事項！\n1.餐後吃、運動後30內飲用\n2.空腹食用無法有保健作用\n3.不要過度加熱、與酸性飲料混雜、加太多糖或鹽\n4.早餐量應整天50%，剩下給中餐和晚餐\n5.狂喝不代表長肌肉，過量可能發胖\n6. 肝腎病患慎吃、3歲以下禁吃'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '健身多快能看見成果？' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='您是否會急於看見運動後體態改變的成果？\n影響因素有很多，除了運動量外，重要的是開始時的體脂肪！顧及健康的小原則：每個月減少1-2％體脂肪。'))
            messages.append(TextSendMessage(text='以下為體脂率參考值：\n看出腹肌的體脂率男性為6-13％，女性為14-19％\n男性肥胖25%以上 ，女性肥胖32%以上\n男性平均值18-24%，女性平均值25-31%\n男性理想為14-17%，女性理想為21-24%'))
            messages.append(TextSendMessage(text='若您為「肥胖」程度，也許會需要更長時間！\n男性：10個月至2年，女性：1-2年\n若您為「平均值」程度，相信您很快就能達成了！\n男性：3-6個月，女性：1-3個月\n若您為「理想」程度，鍛鍊起來不是問題！\n男性：4-6週，女性：腹肌已現形或需要數週'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '有段時間沒運動，身材會荒廢' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='當肌肉超過3週以上缺乏鍛鍊時，便可能會產生較為顯著的肌肉流失現象。可以在平日空檔進行一些重量訓練的活動，也能在家中透過徒手訓練的方式。'))
            messages.append(TextSendMessage(text='3~4個禮拜的休息，會在進行有氧運動時的心肺耐力下降4~25%。重新回歸訓練雖然會因為肌力明顯衰退，而感到不少沮喪和失落，但是肌肉記憶可以幫助您快速重新回到增肌的跑道。只要再次建立規律的運動習慣，回復理想的運動表現和身材並不是難事。'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '吃點心都會覺得罪惡感高!' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='別這麼想！\n暴食和節食的惡性循環從責怪自己開始，所以當吃完美食後不應該馬上測量體重，因為吃進肚子裡的食物有重量，因此不但不準確，還會使自己不愉快。'))
            messages.append(TextSendMessage(text='以下是飽餐一頓後的小建議：\n1.多走路散步，幫助消化\n2.充足睡眠能增加瘦體素，管理食慾\n3.聚餐變成生活一部分，不害怕其影響\n4.用平常心看待飲食，使身心達到平衡'))
            line_bot_api.reply_message(event.reply_token, messages)
            messages.append(service_or_not)
        elif '吃外食還能維持好身材嗎' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='若您為平日較匆忙的人，也不必擔心一直吃外食會讓身材走樣，除了避免長時間久坐之外，均衡飲食的觀念非常重要，且每餐的蔬菜量最好大於肉類，並讓飲食保持多元化！'))
            messages.append(TextSendMessage(text='飲食避免：\n1.避免重口味的習慣\n2.濃湯、勾芡類型湯品\n3.油煎、油炸、 糖醋、燴的製作方式'))
            messages.append(TextSendMessage(text='飲食小建議：\n1.少鹽、少油、少糖、少醬料\n2.選擇蒸、煮、清燉和涼拌等的料理\n3.天然食材較不易使血糖突然升高，所含的熱量較低。'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '基礎代謝率是什麼' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='BMR：基礎代謝率\n即使躺著不動，身體各器官工作需要消耗能量，來維持身體機能，而這樣的能量就被稱為「Basal Metabolic Rate」。'))
            messages.append(TextSendMessage(text='第一個算法：\n男性： 5+(13.7*KG)+(5*CM)-(6.8*年紀)\n女性：基礎代謝率 =655+(9.6*KG)+(1.8*CM)-(4.7*年紀)'))
            messages.append(count_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '每日總消耗熱量是什麼' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='我們吃進食物後，身體要負責消化食物和吸收營養，消化與吸收都需要耗費能量。年紀、性別、基因是我們考慮代謝力時難以調控的部分，而體重較重的時候，基礎代謝率是比較高的，藉著節食反而會放慢新陳代謝。'))
            messages.append(TextSendMessage(text='算法：\n無活動：久坐\nTDEE = 1.2x BMR\n輕量活動：每周運動1-3天(輕鬆)\nTDEE = 1.4 x BMR\n中度活動量：每周運動3-5天\nTDEE = 1.6 x BMR\n高度活動量：每周運動6-7天\nTDEE = 1.8 x BMR\n非常高度活動量：\n無時無刻高強度的運動，像是建築工人等勞力型的工作\nTDEE = 2x BMR'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '改變代謝力' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='從飲食改變代謝力：\n1.增加蛋白質攝取量，因為身體在消耗蛋白質上相對耗能\n2.餐前飲用300cc水量\n3.嘗試以咖啡、綠茶燃燒的效果較短暫且有限'))
            messages.append(TextSendMessage(text='從體能活動改變代謝力：\n‧高強度間歇訓練：(TABATA模式、HIIT)\n1.休息時的代謝能力上升，對葡萄糖的代謝、運用變好\n2.有效地減少脂肪量，比有氧額外燃燒25%卡路里\n3.為了適應運動強度，心臟肌肉也更強壯'))
            messages.append(TextSendMessage(text='從體能活動改變代謝力：\n‧阻力訓練、舉重\n1.增加骨骼肌肌力、肌耐力、和肌肉質量\n2.刺激荷爾蒙生成，神經傳導變好，並增強\n3.刺激骨骼肌裡的蛋白質合成'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '跟我說有關挑選自助餐的事吧' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text=' 掌控預算，健康挑起來！'))
            messages.append(TextSendMessage(text='提醒：\n1.選擇多色多樣的蔬菜(含菇類)\n2.選高纖碳水(雜糧、地瓜、紅蘿蔔)\n3.蛋白質以原型為主\n4.豆製品是好的選擇(豆干,豆腐)'))
            messages.append(TextSendMessage(text='避免：\n1.炸蔬菜跟肉(醬拌茄子、炸排骨)\n2.含油量高的肉(香腸、糖醋排骨)\n3.勾芡的羹湯濃湯或麻婆豆腐'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '想吃想吃，有甚麼該注意的' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='放縱一下，聚會約起來！'))
            messages.append(TextSendMessage(text='提醒：\n1.火鍋可選清湯、增加蔬菜\n2.低脂肉類(蝦、魚、雞鴨、里肌)\n3.調味以天然香料(蔥、蒜、辣椒)\n4.義大利麵以清炒、茄汁較佳'))
            messages.append(TextSendMessage(text='避免：\n1.加工料、丸餃類\n2.炸豆皮、百頁豆腐等炸彈\n3.燒烤、火鍋等注意沾醬\n4.高脂肉類(霜降肉、五花肉、培根片、翅膀'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '有關水果，我該知道甚麼呢' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='甜甜點心，營養補起來！'))
            messages.append(TextSendMessage(text='提醒：\n1.越早食用越能被有效利用\n2.做為餐間點心、下午茶\n3.每天約可攝取2~4份水果\n4.一份約為一個拳頭或是切塊一碗\n5.GI值與膳食纖維相關，膳食纖維含量越高，GI值越低\n6.西瓜、龍眼、荔枝、榴槤等高GI水果份量要特別注意'))
            messages.append(TextSendMessage(text='避免：\n1.集中同一餐吃水果，血糖迅飆升\n2.只吃水果取代正餐\n3.榨杯果汁、吃果乾較沒有咀嚼水果的營養效果'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '跟我說說選飲料的大學問' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='口渴難耐，愉快訂起來！'))
            messages.append(TextSendMessage(text='提醒：\n1.以奶類取代奶精\n2.配料建議以愛玉、仙草、山粉圓\n3.選去冰、常溫的較佳\n4.容量選中或小杯，滿足就好'))
            messages.append(TextSendMessage(text='避免：\n1.甜度要小心(全糖200卡半糖100卡微糖60卡)\n2.少選酸的飲料，製程會添加更多的糖\n3.珍珠、粉圓、芋圓等澱粉配料少選'))
            messages.append(service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)

        elif '給我溫暖' in recrive_text:
            call_ask_mood_templet(event)
        elif '我心情不好嗚嗚嗚' in recrive_text:
            call_why_in_bad_mood(event)
        elif '我努力了，但看不到成果QAQ' in recrive_text:
            badmood_reason_one(event)
        elif '最近在生活中遇到讓我難過的事...' in recrive_text:
            badmood_reason_two(event)
        elif '你不懂我啦...' in recrive_text:
            badmood_reason_three(event)
        elif '我今天心情普普通通通啦' in recrive_text:
            call_soso_mood(event)
        elif '我現在心情超級好的啦' in recrive_text:
            call_good_mood(event)
        elif '給你看給你看' in recrive_text:
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1990))
            messages.append(TextSendMessage(text='好的，請傳一張你的局部肌肉照片給我(我可以辨識手、腳、胸腹、背)'))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '我先pass' in recrive_text:
            messages=[]
            messages.append(StickerSendMessage(package_id=446, sticker_id=1989))
            messages.append(TextSendMessage(text='齁~對自己有自信一點啦~啊也不要擔心我是變態(這我可以發誓我絕對不是嗚嗚嗚嗚'))
            messages.append(TextSendMessage(text='沒事，那我們下次再玩~'))
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif '計算BMI' in recrive_text:
            call_BMI(event)
        else:
            calculate_BMI(event,recrive_text)

    elif event.message.type=='sticker':
        receive_sticker_id=event.message.sticker_id
        receive_package_id=event.message.package_id
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id=receive_package_id, sticker_id=receive_sticker_id))
    elif event.message.type=='image':
        message_content = line_bot_api.get_message_content(event.message.id)
        with open('.\\static\\temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        image = Image.open('.\\static\\temp_image.png')
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        # run the inference
        prediction = model.predict(data)
        results=('胸前', '背肌', '手臂', '腿腿', '無法辨識')
        numerical_result=prediction.argmax()
        if numerical_result == 0:
            messages=[]
            messages.append(TextSendMessage(text=f'你的{results[numerical_result]}在發光...你居然把自己變成了巧克力？！？'))
            messages.append(TextSendMessage(text='你是狠角色，給你100分'))
            messaegs.append(StickerSendMessage(package_id=11538, sticker_id=51626498))
            messages.append(StickerSendMessage(package_id=happysticker[0], sticker_id=happysticker[1]))
            messaegs.append(StickerSendMessage(package_id=11537, sticker_id=52002734))
            line_bot_api.reply_message(event.reply_token, messages)

        elif numerical_result == 1:
            messages=[]
            picture_my_goal='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmN5J1cf3n8LR9ffgln1KTXz_ECPPj83yIyg&usqp=CAU'
            messaegs.append(StickerSendMessage(package_id=11537, sticker_id=52002747))
            messages.append(f'你的{results[numerical_result]}好美，gorgeous!!!')
            messages.append('給你的背100分，我超喜歡！！！')
            messages.append('跟你分享我偶像羅尼庫爾曼的背肌')
            messages.append(ImageSendMessage(original_content_url=picture_my_goal, 
                                            preview_image_url=picture_my_goal))
            line_bot_api.reply_message(event.reply_token, messages)

        elif numerical_result == 2:
            messages=[]
            picture_dogdog='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT49akGsXV5-s6tHwa1b-XaCwSCAtDjkfhiSQ&usqp=CAU'
            messages.append(TextSendMessage(text=f'你的{results[numerical_result]}練得很棒欸！！！你沒有辜負你之前的努力嗚嗚嗚'))
            messages.append(TextSendMessage(text='雖然你已經100分了，但還要繼續朝著你的夢想前進！！！'))
            messages.append(TextSendMessage(text='(給你看可愛的巨巨柴柴'))
            messages.append(ImageSendMessage(original_content_url=picture_dogdog, 
                                            preview_image_url=picture_dogdog))
            line_bot_api.reply_message(event.reply_token, messages)
            
        elif numerical_result == 3:
            messages=[]
            picture_leg='https://www.lovely-dogs.com/image/blog/famous-fat-cat-who-inspired-meme-honored-with-statue-1.jpg'
            messages.append(TextSendMessage(text=f'是{results[numerical_result]}！！你的{results[numerical_result]}怎麼這麼好看'))
            messages.append(TextSendMessage(text='me be like：'))
            messages.append(ImageSendMessage(original_content_url=picture_leg, 
                                        preview_image_url=picture_leg))
            messages.append(TextSendMessage(text='你真的超強的！比我強太多了！！(慚愧'))
            line_bot_api.reply_message(event.reply_token, messages)

        else:
            messages=[]
            messages.append(TextSendMessage(text='ㄨㄚ'))
            messages.append(TextSendMessage(text='我看不出來你在哪裡...我的視力不好，金拍謝！！！'))
            messages.append(TextSendMessage(text='你可以再傳一張比較清楚/只有特定部位的照片給我'))

    elif event.message.type=='audio':
        filename_wav='temp_audio.wav'
        filename_mp3='temp_audio.mp3'
        message_content = line_bot_api.get_message_content(event.message.id)
        with open(filename_mp3, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        os.system(f'ffmpeg -y -i {filename_mp3} {filename_wav} -loglevel quiet')
        text = transcribe(filename_wav)
        # print('Transcribe:', text)
        if '服務' in text:
            # print(url_for('static', filename='images/brown_1024.jpg', _external=True))
            call_introduction(event)

another_service_or_not = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='請問還需要其他機器的介紹嗎?',
        actions=[
            PostbackAction(
                label='還需要',
                display_text='還需要',
                data='action=還需要其他介紹'
            ),
            PostbackAction(
                label='暫時先不用',
                display_text='暫時先不用',
                data='action=暫時先不用其他介紹'
            )
        ]
    )
)

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)
