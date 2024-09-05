import random

def roll_dice(sides, rolls):
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

sides = int(input("Enter the number of sides on the dice: "))
rolls = int(input("Enter the number of rolls: "))

results = roll_dice(sides, rolls)
print(f"Results: {results}")
