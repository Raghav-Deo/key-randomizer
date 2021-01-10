from random import shuffle, random
from datetime import datetime
import string
import secrets


def key_randomizer(original_key):
    key3 = original_key.strip()
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
    final_key = str(magic) + str(var4) + str(key2)
    return final_key


def password_saver(output):
    var = datetime.now()
    var1 = '\n' + 'New Password = ' + '' + output + '     ' + var.strftime("\n%b-%d-%Y   %H:%M:%S\n")
    with open("password.txt", "a") as file:
        file.write(var1)
