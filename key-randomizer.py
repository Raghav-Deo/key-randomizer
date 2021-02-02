#!/usr/bin/env python3


from Packages.main import key_randomizer


if __name__ == '__main__':
    key_randomizer.intro()
    key_randomizer = key_randomizer(input("Give your password here : "))
    output = key_randomizer.password_generator()
    print(output+'\nThis is your key,this key will also be saved in a text file named as password.txt\nThanks for '
                 'using our tool !\n(Ignore the text shown below)')
    key_randomizer.process_completed()
    key_randomizer.password_saver()
    key_randomizer.password_saved()
    quit()
elif __name__ != '__main__':
    print("You are not allowed to run this program by importing it\nExiting!")
else:
    print("An unknown error occurred while executing the program")
