# create snake and ladder board 
import random

try:
    snakes = random.sample(range(2, 100), 10)
    print(" Snake heads are at positions:", snakes)
    print("\n---Snake & Ladder Board (1–100) ---\n")

    # Print 
    
    for i in range(100, 0, -10):
        row = list(range(i - 9, i + 1))
        # Reverse  pattern
        if (i // 10) % 2 == 0:
            row.reverse()
        for num in row:
            if num in snakes:
                print(f"{num:3}>:", end=" ")  # head 
            else:
                print(f"{num:3}", end=" ")
        print()

except Exception as e:
    print("Error:", e)