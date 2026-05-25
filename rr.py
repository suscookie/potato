import random
import time

chambers = int(input("Enter the number of chambers: "))
kill_bullet = random.randint(1, chambers)

while True:
    
    chosen_chamber = random.randint(1, chambers)
    
    input("Press ENTER to spin and shoot the barrel.")
    print("Spinning the barrel and shooting...")
    time.sleep(1)
    if kill_bullet == chosen_chamber:
        print("You have died.")
        break
    else:
        print("You live to see another day.")
    
    choice = input("Do you want to continue? (y/n): ")
    choice = choice.lower()
    if choice[0] == "y":
        continue
    else:
        break
    
    

