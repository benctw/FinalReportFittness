# import flask related
import re
from flask import Flask, request, abort, url_for, render_template
from urllib.parse import parse_qsl, parse_qs
import random
from linebot.models import events
from line_chatbot_api import *
from service_actions.BMI import *
from service_actions.introduction import *

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
import speech_recognition as sr

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
    user_id = event.source.user_id
    user_name = line_bot_api.get_profile(user_id).display_name
    # print(event.postback.data)
    postback_data = dict(parse_qsl(event.postback.data))
    # print(postback_data.get('action', ''))
    # print(postback_data.get('item', ''))
    sticker_list=[(1070, 17839), (6362, 11087920), (11537, 52002734), (8525, 16581293)]
    if postback_data.get('action')=='索取備品':
        sticker_random=sticker_list[random.randint(0,len(sticker_list)-1)]
        messages=[]
        messages.append(StickerSendMessage(package_id=sticker_random[0], sticker_id=sticker_random[1]))
        messages.append(TextSendMessage(text=f'{user_name}, 好的沒問題, 櫃台服務人員將盡快幫您準備{postback_data.get("item", "")}'))
        messages.append(another_service_or_not)
        line_bot_api.reply_message(event.reply_token, messages)
    elif postback_data.get('action')=='還需要其他介紹':
        call_service(event)  
    elif postback_data.get('action')=='暫時先不用其他介紹':
        messages=[]
        messages.append(StickerSendMessage(package_id=11537, sticker_id=52002734))
        messages.append(TextSendMessage(text='祝您有愉快的健身體驗'))
        line_bot_api.reply_message(event.reply_token, messages)

@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        recrive_text=event.message.text
        # print(recrive_text)
        if '器材操作說明' in recrive_text:
            # print(url_for('static', filename='images/brown_1024.jpg', _external=True))
            call_service(event)
        elif '我想知道跑步機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://i.imgur.com/H8O5GVT.png', preview_image_url='https://i.imgur.com/JM2MHSi.png'))
            messages.append(TextSendMessage(text='跑步機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages)  
        elif '我想知道滑步機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://i.imgur.com/H8O5GVT.png', preview_image_url='https://i.imgur.com/JM2MHSi.png'))
            messages.append(TextSendMessage(text='滑步機介紹待定'))
            messages.append(another_service_or_not)
            line_bot_api.reply_message(event.reply_token, messages) 
        elif '我想知道划船機怎麼用' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://i.imgur.com/H8O5GVT.png', preview_image_url='https://i.imgur.com/JM2MHSi.png'))
            messages.append(TextSendMessage(text='划船機機介紹待定'))
            messages.append(another_service_or_not)
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
        with open('temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
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
            call_service(event)

another_service_or_not = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='請問還需要其他介紹嗎?',
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