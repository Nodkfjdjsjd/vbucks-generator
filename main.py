import time
import random

def give_vbuck(Nokia2000 ultra, 1000):
    print(f"Giving my boy {Nokia2000 ultra} {1000} vbucks.")

    time.sleep(5)

    success = random.choice([True, False])

    if success:
        print("Success! Now you can buy floss emote and renegade raider!")
    else:
        print("Invalid username lmao")

give_vbuck(
    input("What's your username? "),
    int(input("How much vbuck? "))
)
