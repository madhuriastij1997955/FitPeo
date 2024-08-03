# Input
currentstate_size = int(input())
currentstate = list(map(int, input().split()))
days = int(input())


# Function to calculate the next state of street lights
def calculate_next_state(currentstate):
    nextstate = [0] * currentstate_size  # Initialize a list for the next state
    for i in range(currentstate_size):
        # Determine the next state based on the current state and its neighbors
        if i == 0:
            nextstate[i] = currentstate[i] or currentstate[i + 1]
        elif i == currentstate_size - 1:
            nextstate[i] = currentstate[i - 1] or currentstate[i]
        else:
            nextstate[i] = currentstate[i - 1] or currentstate[i] or currentstate[i + 1]
    return nextstate


# Simulate the state changes for M days
for _ in range(days):
    currentstate = calculate_next_state(currentstate)

print(*currentstate)
