import random

while True:

    computerChoiceNum = random.randint(1,3)
    choices = {1: "rock" , 2: "paper", 3: "scissors"}
    computerChoice = choices[computerChoiceNum]

    user_input = input("Enter your choice (rock, paper, scissors): ").lower()

    # check condition
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice")
        continue

    print(f"Computer chose: {computerChoice}")

    # So sánh and choose winner
    if user_input == computerChoice:
        print("Play again.\n")
        continue

    elif (user_input == "rock" and computerChoice == "scissors") or (user_input == "scissors" and computerChoice == "paper") or (user_input == "paper" and computerChoice == "rock"):
        print("You win")
    else:
        print("Computer Win")

    break






