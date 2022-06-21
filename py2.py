import random

health=50
diff=3



potion_health=int(random.randint(25,50)/diff)

health=health+potion_health

print(health)

