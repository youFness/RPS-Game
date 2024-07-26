import random
from collections import Counter

def player(prev_play, opponent_history=[]):
    # Track the opponent's play history
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize strategies and attributes
    if not hasattr(player, "strategy_index"):
        player.strategy_index = 0
        player.strategies = [random_strategy, frequency_strategy, pattern_strategy]

    # Change strategy periodically (every 10 games)
    if len(opponent_history) % 10 == 0:
        player.strategy_index = (player.strategy_index + 1) % len(player.strategies)

    # Execute the current strategy
    return player.strategies[player.strategy_index](opponent_history)

# Random strategy
def random_strategy(opponent_history):
    return random.choice(["R", "P", "S"])

# Frequency-based strategy
def frequency_strategy(opponent_history):
    if len(opponent_history) > 0:
        most_common = Counter(opponent_history).most_common(1)[0][0]
        return counter_response(most_common)
    return random.choice(["R", "P", "S"])

# Pattern-based strategy
def pattern_strategy(opponent_history):
    if len(opponent_history) >= 2:
        last_move = opponent_history[-1]
        return counter_response(last_move)
    return random.choice(["R", "P", "S"])

# Function to get the counter response
def counter_response(move):
    return {"R": "P", "P": "S", "S": "R"}[move]

# Bind strategies to player function
player.random_strategy = random_strategy
player.frequency_strategy = frequency_strategy
player.pattern_strategy = pattern_strategy
