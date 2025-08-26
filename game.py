import os
import time
import random
from datetime import datetime

CHOICES = ["Rock", "Paper", "Scissors"]
RULES = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

def play_once():
    p1 = random.choice(CHOICES)
    p2 = random.choice(CHOICES)
    print(f"[{datetime.utcnow().isoformat()}Z] Player1: {p1} | Player2: {p2}")

    if p1 == p2:
        print("Result: Draw!\n", flush=True)
    elif RULES[p1] == p2:
        print("Result: Player 1 wins!\n", flush=True)
    else:
        print("Result: Player 2 wins!\n", flush=True)

if __name__ == "__main__":
    rounds = int(os.getenv("RPS_ROUNDS", "0"))
    interval = float(os.getenv("RPS_INTERVAL_SEC", "2"))

    if rounds <= 0:
        while True:
            play_once()
            time.sleep(interval)
    else:
        for _ in range(rounds):
            play_once()
            time.sleep(interval)
