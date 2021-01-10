from Packages.main import key_randomizer, password_saver
print("Coded and maintained by Raghav Deo")
output = key_randomizer(input("Give your password here : "))
print("Thanks for using our tool !")
print(output)
print("This is your key,this key will also be saved in a text file named as password.txt")
print("Thanks for using our tool !")
password_saver(output=output)
quit()
