user = input("What is your name?")
temp = input("What is the temperature outside today, {0}?".format(user))
user2 = input("Are you going outside today, {0}? Enter 1 for yes, 0 for no.".format(user))
if user2 is str(0):
    if temp < 69:
        print("That makes sense, as the temperature is {0}. Have a nice day, {1}.".format(temp, user))
    if temp > 70:
        print("You really should, {0}! The temperature is a warm {1}.".format(user, temp))
if user2 is str(1):
    if int(temp) < 69:
        print("Wear pants, {0}.".format(user))
    if int(temp) > 70:
        print("Wear shorts, {0}! And be grateful you're not a computer!".format(user))