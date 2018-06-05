import sys

import pyttsx3


class Speeker:

    def __init__(self):
        self.voice = pyttsx3.init()

    def say(self, msg):
        self.voice.say(msg)
        self.voice.runAndWait()
        self.voice.stop()


if __name__ == '__main__':
    msg = sys.argv[1]
    sp = Speeker()
    sp.say(msg)