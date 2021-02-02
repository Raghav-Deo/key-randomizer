import secrets
import string
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
from random import shuffle, random


class key_randomizer():
    def __init__(self, original_key):
        self.original_key = original_key
        self.final_key = None

    @staticmethod
    def intro():
        print("Coded and maintained by Raghav Deo")

    def password_generator(self):
        key3 = self.original_key.strip()
        key1 = list(key3)
        for i in range(10):
            shuffle(key1)
        key2 = str(random())
        var = ''.join(key1)
        var1 = var.replace('[', '')
        var2 = var1.replace(']', '')
        var3 = var2.replace(',', '')
        var4 = var3.replace("'", "")
        magic = str(secrets.choice(string.ascii_letters)) + str(secrets.choice(string.ascii_lowercase)) + str(
            secrets.choice(string.ascii_uppercase)) + str(secrets.choice(string.punctuation))
        self.final_key = str(magic) + str(var4) + str(key2)
        return self.final_key

    def process_completed(self):
        file = AudioSegment.from_file('MFSLlGNQlc')
        play(file)

    def password_saver(self):
        var = datetime.now()
        var1 = '\n' + 'New Password = ' + '' + self.final_key + '     ' + var.strftime("\n%b-%d-%Y   "
                                                                                       "%H:%M:%S\n")
        with open("password.txt", "a") as file:
            file.write(var1)
            file.close()

    def password_saved(self):
        file = AudioSegment.from_file('pvMVfDp5xT')
        play(file)
