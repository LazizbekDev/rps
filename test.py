import sys
import random

print("")
player = int(input("Enter pls...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n"))
computer = int(random.choice('123'))

if player < 1 | player > 3:
    sys.exit("\033[7m You must enter 1, 2 or 3\033[0m")

print("")
print(f"\033[2mPlayer cose: {player}\033[0m")
print(f"\033[2mBot chose: {computer}\033[0m")

if player == 1 and computer == 2:
    print("\033[7mYou win!\033[0m")
elif player == 2 and computer == 1:
    print("\033[7mYou win!\033[0m")
elif player == 3 and computer == 2:
    print("\033[7mYou win!\033[0m")
elif player == computer:
    print("\033[7mTie game\033[0m")
else:
    print("\033[7mBot win!\033[0m")