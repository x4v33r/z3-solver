# coding: utf-8
import os, sys, subprocess
import time
from z3 import *

CHOICES = ["Rock", "Paper", "Scissors", "Spock", "Lizard"]


def next_random_number(s_i):
    return ((11 * s_i) + 12345) & 0x7FFF


class RPSSLComputer:
    def __init__(self, s0):
        self.previous_random_number = s0

    def compute_choice(self):
        random_number = next_random_number(self.previous_random_number)
        self.previous_random_number = random_number
        return random_number % 5, CHOICES[random_number % 5]


# cf. https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock
def winning_mapping(i):
    if i == 0:
        return 1  # "Paper"
    if i == 1:
        return 2  # "Scissors"
    if i == 2:
        return 0  # "Rock"
    if i == 3:
        return 4  # "Lizard"
    if i == 4:
        return 0  # "Rock"
    return "Did you forget to compute the remainder modulo 5?"


def compute_winner(computer, player):
    if computer == player:
        return "\tTie.", False
    is_player_bigger = True if player > computer else False
    absolute_difference = abs(computer - player)
    if absolute_difference % 2 == 1:
        if is_player_bigger:
            return "\tPlayer wins.", True
        else:
            return "\tComputer wins.", False
    else:
        if is_player_bigger:
            return "\tComputer wins.", False
        else:
            return "\tPlayer wins.", True


solver = Solver()
states = list()

# We are adding the first state s_0 to the list of states
states.append(BitVec("state0", 16))

s0 = int(sys.argv[1])
computer = RPSSLComputer(s0)

preprocess_count = 5


def add_constraint(solver, index, computers_choice):
    # TODO create a BitVec and append it to the list of states
    # You might want to call it state{index}
    new_state = BitVec(f"state{index}", 16)
    states.append(new_state)

    # TODO Enforce that the newly added BitVec-variable must evaluate to the result of the LCG computation using the previous result
    compute = 11 * states[index - 1] + 12345 & 0x7FFF
    solver.add(new_state == compute)

    # TODO Enforce that the unsigned remainder of the newly added BitVec-varialbe and 5 evaluates to the choice of the computer
    remainder = URem(new_state, 5)
    solver.add(remainder == computers_choice)

    pass


def store_backtracking_point(solver):
    solver.push()


def restore_backtracking_point(solver):
    solver.pop()


def add_next_state_constraint(solver):
    s_i_plus_1 = BitVec("s_i_plus_1", 16)
    # TODO Enforce that the next state value is computed via the same computation as above
    compute = 11 * states[len(states) - 1] + 12345 & 0x7FFF
    solver.add(s_i_plus_1 == compute)

    return s_i_plus_1


def get_players_choice(solver, s_i_plus_1):
    # TODO Get the value of next_state from the model and return it modulo 5
    # Hint: winning_mapping(...) returns a good answer for the computer's choice
    # Hint: use solver.model() like a python dict.
    # Hint: use `.as_long()` to convert a z3 variable to a python integer value
    next_state = solver.model()[s_i_plus_1].as_long()
    return winning_mapping(next_state % 5)

    #return 0


# Main loop:

# We read preprocess_count many choices from the computer before we start to ask z3 for a solution
# Note that for these preprocessing rounds we do not need to make a good guess and compute the winner
# We are only interested in what the computer picks for the first few rounds
for index in range(1, preprocess_count):
    computer_choice, _ = computer.compute_choice()
    player_choice = (
        0  # We always choose Rock since we cannot make good guesses in the beginning
    )

    add_constraint(solver, index, computer_choice)
    output, won = compute_winner(computer_choice, player_choice)
    print(output)
    if won:
        print("Congratulations!")
    else:
        print("Try again.")


# Now we start by adding a 'special' variable s_i_plus_1 and try to win
index = preprocess_count
while True:
    store_backtracking_point(solver)
    s_i_plus_1 = add_next_state_constraint(solver)
    solver.check()

    player_choice = get_players_choice(solver, s_i_plus_1)
    computer_choice, _ = computer.compute_choice()
    output, won = compute_winner(computer_choice, player_choice)

    print(output)
    if won:
        print("Congratulations!")
    else:
        print("Try again.")

    restore_backtracking_point(solver)
    add_constraint(solver, index, computer_choice)
    # input("")
    index += 1
    if index >= 100:
        break
