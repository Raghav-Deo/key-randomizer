from random import shuffle
from random import random
import os
import sys
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
    magic = str(secrets.choice(string.ascii_letters))+str(secrets.choice(string.ascii_lowercase))+str(secrets.choice(string.ascii_uppercase))+str(secrets.choice(string.punctuation))
    final_key = str(magic) + str(var4) + str(key2)
    return final_key


print("Coded and maintained by Raghav Deo")
output = key_randomizer(input("Give your password here : "))
print("This is your key,this key will also be saved in a text file named as password.txt")
print("Thanks for using our tool !")
print(output)
if os.path.exists("password.txt"):
    sys.stdout = open("password1.txt", "w")
    print(output)
    sys.stdout.close()
if not os.path.exists("password.txt"):
    sys.stdout = open("password.txt", "w")
    print(output)
    sys.stdout.close()
quit()
