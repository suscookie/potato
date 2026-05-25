import random
import time

print("=== Russian Roulette Simulator ===")
print("6 chambers. 1 bullet.\n")

while True:
    input("Press ENTER to pull the trigger...")

    chamber = random.randint(1, 6)

    print("Spinning cylinder...")
    time.sleep(1)

    if chamber == 1:
        print("💥 BANG! You lost.")
        break
    else:
        print("Click... You survived.\n")