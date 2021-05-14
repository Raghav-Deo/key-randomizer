import secrets
import string
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
from random import shuffle, random


class Keyrandomizer:
    def __init__(self, original_key):
        self.original_key = original_key
        self.final_key = None

    @staticmethod
    def intro():
        print("Coded and maintained by Raghav Deo")

    def password_generator(self):
        key1 = list(self.original_key.strip())
        for i in range(10):
            shuffle(key1)
        magic = "{} {} {} {}".format(str(secrets.choice(string.ascii_letters)), str(secrets.choice(string.ascii_lowercase)), str(secrets.choice(string.ascii_uppercase)), str(secrets.choice(string.punctuation)))
        self.final_key = "{} {} {}".format(str(magic), str(''.join(key1).replace('[', '').replace(']', '').replace(',', '').replace("'", "")), str(random()))
        return self.final_key

    @staticmethod
    def process_completed():
        file = AudioSegment.from_file('MFSLlGNQlc')
        play(file)

    def password_saver(self):
        garb = datetime.now()
        arg = "\n New Password = {}\n{}\n".format(self.final_key, garb.strftime('%b-%d-%Y, %H:%M:%S'))
        with open("password.txt", "a") as file:
            file.write(arg)
            file.close()

    @staticmethod
    def password_saved():
        file = AudioSegment.from_file('pvMVfDp5xT')
        play(file)
