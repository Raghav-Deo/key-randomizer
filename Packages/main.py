import secrets
import string
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
from random import shuffle, random


class Keyrandomizer:
    def __init__(self, original_key):  # Constructor method
        self.original_key = original_key  # initializing data member for original key
        self.final_key = None  # initializing data member for final key i.e. randomized key

    @staticmethod
    def intro():  # A method for introduction
        print("Coded and maintained by Raghav Deo")

    def password_randomizer(self):  # A method to randomize the password which returns randomized password
        key1 = list(self.original_key.strip())
        for i in range(10):
            shuffle(key1)
        magic = "{} {} {} {}".format(str(secrets.choice(string.ascii_letters)), str(secrets.choice(string.ascii_lowercase)), str(secrets.choice(string.ascii_uppercase)), str(secrets.choice(string.punctuation)))
        self.final_key = "{} {} {}".format(str(magic), str(''.join(key1).replace('[', '').replace(']', '').replace(',', '').replace("'", "")), str(random()))
        return self.final_key

    @staticmethod
    def process_randomized_audio():  # Method to play the audio file
        file = AudioSegment.from_file('.MFSLlGNQlc')
        play(file)

    def password_saver(self):  # Method to save the randomized password and add time and date stamps
        garb = datetime.now()
        arg = "\n New Password = {}\n{}\n".format(self.final_key, garb.strftime('%b-%d-%Y, %H:%M:%S'))
        with open("password.txt", "a") as file:
            file.write(arg)
            file.close()

    @staticmethod
    def password_saved_audio():  # Method to play the audio file
        file = AudioSegment.from_file('.pvMVfDp5xT')
        play(file)
