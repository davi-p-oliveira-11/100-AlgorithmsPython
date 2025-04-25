# russian roulette

import random
import time

print("Spinning the chamber...")
time.sleep(1.5)
print("Pulling the trigger...")
time.sleep(1.5)

if random.randint(1,6) == 1:
  print("💥 Bang Goodbye ! 💀💀💀")
else:
  print("😮‍💨 Click. You got lucky this time.")