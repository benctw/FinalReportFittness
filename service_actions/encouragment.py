from urllib.parse import parse_qsl, parse_qs
import datetime, random, json

from linebot.models import messages
from line_chatbot_api import *

sadsticker_list=[]
sadsticker_list.append((6362, 11087930))
sadsticker_list.append((8525, 16581310))
sadsticker_list.append((11537, 52002750))
sadsticker_list.append((11537, 52002755))
sadsticker_list.append((11538, 51626529))
sadsticker_list.append((11539, 52114138))
sadsticker_list.append((11539, 52114137))

happysticker_list=[]
happysticker_list.append((11539, 52114146))
happysticker_list.append((11539, 52114118))
happysticker_list.append((11539, 52114122))
happysticker_list.append((11538, 51626496))
happysticker_list.append((8525, 16581300))
happysticker_list.append((6362, 11087942))

fittness_list=[]
fittness_list.append('所有偉大的事，都是在堅持過後才實現的')
fittness_list.append('你不會因為你失敗了這幾次，而永遠的失敗下去。')
fittness_list.append('事情總是看起來非常艱難，直到最後完成了，你才會發現自己其實很厲害')
fittness_list.append('你走得多慢都沒關係，最重要的是不要停下你的腳，繼續往前走！')
fittness_list.append('水滴終可磨損大石，不是因為它力量強大，而是因為它不停不停的滴。你想要你的身材越來越好看，那就不要放棄！')
fittness_list.append('別放棄你的夢想，讓他帶著你飛！')

ending_list=[]
ending_list.append('加油！我知道你一定OK的')
ending_list.append('fighting!!!You can do it!!!')
ending_list.append('我相信你一定做得到')
ending_list.append('你要知道你超強的，拾起自信再出發！')
ending_list.append('成為夢想中的自己吧！')
ending_list.append('你做不到誰做得到？加油啊啊啊')

compatation_list=[]
compatation_list.append('不管前方的路有多苦，只要走的方向正確，不管多麼崎嶇不平，都比站在原地更接近幸福。你需要的是傾聽自己內心真實的感覺，接下來就交由努力和直覺去做吧！')
compatation_list.append('很多時候，人生就是在絕望與希望間徘徊，每一個活生生人，都要給自己一個目標，且不管這目標是高尚還是低俗。人們沿路走去，有陽光，也會有陰霾。你要知道人生就是由低潮高潮相互交織而成的，對於低潮，你應該要用和迎接自己的快樂時的心態去接納他。這很正常，所以不要害怕它。')
compatation_list.append('把昨天當作回憶，今天繼續努力，明天就隨他去！有努力就好了，如果試了很多次還是不成功，那放下它也未嘗不可，請多愛自己一點！')
compatation_list.append('專注於當下的感受，忽視外在不必要的聲音，這樣應該能讓你好很多。停下來想想看自己想要的到底是什麼，休息也是一種前進的方式喔。')
#compatation_list.append('')
#compatation_list.append('')

meme_list=[]
meme_list.append('https://i.imgur.com/Adcbhcd.jpg')
meme_list.append('https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1603964582148.jpg')
#meme_list.append('')
meme_list.append('https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1629478254752.jpg')
meme_list.append('https://cdn2.ettoday.net/images/1595/d1595053.jpg')
meme_list.append('https://images2.gamme.com.tw/news2/2019/59/91/qaCXoaWekaaWrqU.jpg')

greeting_list=[]
greeting_list.append('嘿，看來最近你的狀況不錯~真是不錯！那這樣你應該不需要我說太多話吧哈哈哈，繼續努力就對了！你的目標：成為健身巨巨！')
greeting_list.append('哇，那表示你最近練得不錯喔~繼續保持你的狀況！keep going！')
greeting_list.append('沒錯沒錯！你已經把訓練的過程用身體記憶起來了！接下來就是持之以恆的朝目標前進！')



def call_ask_mood_templet(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://i.imgur.com/G4XHrYg.jpeg',
            title='嗨呀，最近練的怎麼樣啊？',
            text='別害羞，告訴我你的心情吧xD',
            actions=[
                MessageAction(
                    label='還行',
                    text='我今天心情普普通通通啦'
                ),
                MessageAction(
                    label='so down',
                    text='我心情不好嗚嗚嗚'
                ),
                MessageAction(
                    label='心情很好',
                    text='我現在心情超級好的啦'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def call_why_in_bad_mood(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            #thumbnail_image_url='https://i.imgur.com/G4XHrYg.jpeg',
            title='怎麼啦？也許我可以幫忙？？',
            text='畢竟我是機器人，我能做的很有限，但我會盡量給你溫暖的！！！',
            actions=[
                MessageAction(
                    label='身材遲遲沒進步',
                    text='我努力了，但看不到成果QAQ'
                ),
                MessageAction(
                    label='在生活中遇到挫折',
                    text='最近在生活中遇到讓我難過的事...'
                ),
                MessageAction(
                    label='沒有符合我心情選項',
                    text='你不懂我啦...'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)

def badmood_reason_one(event):
    sadsticker = sadsticker_list[random.randint(0,len(sadsticker_list)-1)]
    saysomething = fittness_list[random.randint(0,len(fittness_list)-1)]
    saysomething2= ending_list[random.randint(0,len(ending_list)-1)]

    messages=[]
    messages.append(StickerSendMessage(package_id=sadsticker[0], sticker_id=sadsticker[1]))
    messages.append(TextSendMessage(text = '跟你說喔，人生本來就超難。在我看來，現在有努力過的你已經超棒了'))
    messages.append(TextSendMessage(text = '也許你現在非常痛苦，但有什麼事不是這樣的嗎？'))
    messages.append(TextSendMessage(text = saysomething))
    messages.append(TextSendMessage(text = saysomething2))

    line_bot_api.reply_message(event.reply_token, messages)

def badmood_reason_two(event):
    happysticker = happysticker_list[random.randint(0,len(happysticker_list)-1)]
    saysomething = compatation_list[random.randint(0,len(compatation_list)-1)]
    messages=[] 
    messages.append(TextSendMessage(text = saysomething))
    messages.append(TextSendMessage(text = '我是機器人，我可能不能完全理解你的感受...'))
    messages.append(TextSendMessage(text = '但是，希望你能趕快恢復你的最佳狀態~'))
    messages.append(TextSendMessage(text = '世界還是很美好的！'))
    messages.append(StickerSendMessage(package_id=happysticker[0], sticker_id=happysticker[1]))
    line_bot_api.reply_message(event.reply_token, messages)

def badmood_reason_three(event):
    meme = meme_list[random.randint(0,len(meme_list)-1)]
    messages=[] 
    messages.append(TextSendMessage(text = 'Hmm...抱歉，我能想到的很有限...'))
    messages.append(TextSendMessage(text = '希望你能快點恢復狀況！！！'))
    messages.append(TextSendMessage(text = '備註：心情不好的時候，去運動會好一點喔~去健健身吧！'))
    messages.append(ImageSendMessage(original_content_url=meme, 
                                        preview_image_url=meme))
    
    line_bot_api.reply_message(event.reply_token, messages)

def call_soso_mood(event):
    greeting = greeting_list[random.randint(0,len(greeting_list)-1)]
    messages=[]
    messages.append(TextSendMessage(text = greeting))
    #messages.append(TextSendMessage(text = '希望你能快點恢復狀況！！！'))
    messages.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            #thumbnail_image_url='https://i.imgur.com/G4XHrYg.jpeg',
            title='要不要來玩一下',
            text='給我看一下你的成果啊~傳一張你局部的肌肉照給我啊',
            actions=[
                MessageAction(
                    label='好啊',
                    text='給你看給你看'
                ),
                MessageAction(
                    label='不了',
                    text='我先pass'
                )
                ]
            )
        ))
    line_bot_api.reply_message(event.reply_token, messages)

def call_good_mood(event):
    messages=[]
    messages.append(TextSendMessage(text = '欸嘿！狀況super的你來玩一下啊'))
    messages.append(TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            #thumbnail_image_url='https://i.imgur.com/G4XHrYg.jpeg',
            title='給我看看你的得意成果啊~',
            text='傳一張你局部的肌肉照給我，讓我看看你到底有沒有認真',
            actions=[
                MessageAction(
                    label='接受',
                    text='給你看給你看'
                ),
                MessageAction(
                    label='婉拒',
                    text='我先pass'
                )
                ]
            )
        ))
    line_bot_api.reply_message(event.reply_token, messages)
