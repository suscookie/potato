import random
import sys

input("Press any key to start...")

while True:
 chambers = input("Please enter the number of chambers (default = 6): ")

 if not chambers:
    chambers = 6

 elif not chambers.isdigit():
    quit("Invalid number of chambers!")

 fatal_bullet = random.randint(1, int(chambers))
 player_survived = True

 for x in range(1, int(chambers) + 1):
    input(f"[{x}/{chambers}] Press enter to pull the trigger! ")
    if x == fatal_bullet:
        print("You just got served!")
        print("Game Over")
        player_survived = False
        break
    print("You survive...for now")
 start_again = input("Do you want to start again? (y/n): ").strip().lower()

 if start_again and start_again.startswith("y"):
    print("and so we go again!!!")
    print("-" * 40)
    continue
 else:
         print("You will live to see another day")
         break
sys.exit()