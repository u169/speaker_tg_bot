import sys
import requests

from gtts import gTTS
import os

def get_answer(question):

    url = "http://p-bot.ru/api/getAnswer"

    headers = {

	"Accept-Encoding":"gzip, deflate",
	"Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
	"Connection":"keep-alive",
	"Content-Length":"1466",
	"Content-Type":"application/x-www-form-urlencoded",
	"Cookie":"dialog_id=ef803de8-1f32-477c-acf2-7b9d6c182c19; dialog_sentiment=0; last_visit=1529489622809::1529500422809",
	"Host":"p-bot.ru",
	"Origin":"http://p-bot.ru",
	"Referer":"http://p-bot.ru/",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
}

    data = {
	"request": question,
	"request_1":"",
	"answer_1":"",
	"request_2":"",
	"answer_2":"",
	"request_3":"",
	"answer_3":"",
	"bot_name":"ρBot",
	"user_name":"Незнакомец",
	"dialog_lang":"ru",
	"dialog_id":"ef803de8-1f32-477c-acf2-7b9d6c182c19",
	"dialog_greeting":"false",
	"a":"public-api",
	"b":"966085348",
	"c":"3842063378",
	"d":"3505844177",
	"e":"0.19556426505001556",
	"t":"1529500448978",
	"x":"3.9678277179379573",
}

    resp = requests.post(url=url, headers=headers, data=data)

    return resp


if __name__ == "__main__":
    user_msg = sys.argv[1]
    print(user_msg)
    
    j = get_answer(user_msg)
    print(j.content)
    answer = j.json()['answer']

    tts = gTTS(text=answer, lang='ru')
    
    name = "{}good.mp3".format(sys.argv[2])
    tts.save(name)
    os.system("mpg321 {}".format(name))
    os.system("rm {}".format(name))
