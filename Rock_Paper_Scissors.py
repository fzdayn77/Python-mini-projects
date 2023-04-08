import random

computer_wins = 0
player_wins = 0
num_draws = 0
possible_inputs = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock / Paper / Scissors or Q to quit the game: ").lower()

    if player_input == "q": break

    if player_input not in possible_inputs: continue
    
    computer_pick = random.randint(0,2)

    if possible_inputs[computer_pick] == player_input:
        print("Draw!\n Player pick: " + player_input.capitalize() + "\n Computer pick: " + possible_inputs[computer_pick].capitalize())
        num_draws += 1
    elif (player_input == "rock" and possible_inputs[computer_pick] == "scissors") or (player_input == "paper" and possible_inputs[computer_pick] == "rock") or (player_input == "scissors" and possible_inputs[computer_pick] == "paper"):
        print("You won!\n Player pick: " + player_input.capitalize() + "\n Computer pick: " + possible_inputs[computer_pick].capitalize())
        player_wins += 1
    else:
        print("You lost!\n Player pick: " + player_input.capitalize() + "\n Computer pick: " + possible_inputs[computer_pick].capitalize())
        computer_wins += 1

print(f'Player wins: {player_wins}\nComputer wins: {computer_wins}\nDraws: {num_draws}')
print("Game ended.")


