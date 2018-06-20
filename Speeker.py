import sys
import requests

from gtts import gTTS
import os

def get_answer(question):

    url = "http://p-bot.ru/api/getAnswer"

    headers = {
        "Host": "p-bot.ru",
        "Connection": "keep-alive",
        "Content-Length": "476",
        "Origin": "http://p-bot.ru",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Referer": "http://p-bot.ru/index.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "dialog_id=ef803de8-1f32-477c-acf2-7b9d6c182c19; dialog_sentiment=0; last_visit=1529484786885::1529495586885"
    }

    data = {
        "request": question,
        "request_1": "",
        "answer_1": "",
        "request_2": "",
        "answer_2": "",
        "request_3": "",
        "answer_3": "",
        "bot_name": "ρBot",
        "user_name": "Незнакомец",
        "dialog_lang": "ru",
        "dialog_id": "ef803de8-1f32-477c-acf2-7b9d6c182c19",
        "dialog_greeting": "false",
        "a": "public-api",
        "b": "1633228958",
        "c": "2843812601",
        "d": "2285551019",
        "e": "0.46171970602024914",
        "t": "1529495617844",
        "x": "4.785864663114257"
    }

    resp = requests.post(url=url, headers=headers, data=data)

    return resp.json()


if __name__ == "__main__":
    user_msg = sys.argv[1]
    
    answer = get_answer(user_msg)['answer']

    tts = gTTS(text=answer, lang='ru')
    
    name = "{}good.mp3".format(sys.argv[2])
    tts.save(name)
    os.system("mpg321 {}".format(name))
    os.system("rm {}".format(name))
