import random

def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Step 1: Place the car behind one random door
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # Step 2: Contestant picks a random door
        contestant_choice = random.randint(0, 2)

        # Step 3: Host opens a door with a goat that is not the contestant's choice
        possible_doors_to_open = [i for i in range(3) if i != contestant_choice and doors[i] == 'goat']
        host_opens = random.choice(possible_doors_to_open)

        # Step 4: Contestant switches their choice
        switch_choice = [i for i in range(3) if i != contestant_choice and i != host_opens][0]

        # Step 5: Check the result
        if doors[switch_choice] == 'car':
            switch_wins += 1
        else:
            stay_wins += 1

    return switch_wins, stay_wins


# Run the simulation
num_trials = 1000000
switch_wins, stay_wins = monty_hall_simulation(num_trials)

print(f"After {num_trials} trials:")
print(f"Wins when switching: {switch_wins} ({switch_wins / num_trials * 100:.2f}%)")
print(f"Wins when staying: {stay_wins} ({stay_wins / num_trials * 100:.2f}%)")
