import sys

from gtts import gTTS
import os


if __name__ == "__main__":
    user_msg = sys.argv[1]

    tts = gTTS(text=user_msg, lang='ru')
    
    name = "{}good.mp3".format(sys.argv[2])
    tts.save(name)
    os.system("mpg321 {}".format(name))
    os.system("rm {}".format(name))
