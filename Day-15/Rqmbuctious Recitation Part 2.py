from typing import Dict

starting_numbers = [0, 14, 6, 20, 1, 4]
n = 30000000

num_to_turn: Dict[int, int] = {
    num: turn for turn, num in enumerate(starting_numbers, start=1)
}

prev_number = starting_numbers[-1]
for turn in range(len(starting_numbers) + 1, n + 1):
    last_turn = turn - 1
    if prev_number in num_to_turn:
        new_number = last_turn - num_to_turn[prev_number]
    else:
        new_number = 0
    num_to_turn[prev_number] = last_turn
    prev_number = new_number
print(prev_number)
