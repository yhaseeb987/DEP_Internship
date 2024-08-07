To run the provided Python program with command-line arguments, you need to follow the syntax specified in the `argparse` section of the script. Here’s a step-by-step guide:

> Command-Line Syntax
python nim_game.py <num_red> <num_blue> <version> <first_player> [--depth <depth>]

Explanation of Arguments
- `<num_red>`: Number of red marbles (integer).
- `<num_blue>`: Number of blue marbles (integer).
- `<version>`: Game version, either `standard` or `misere`.
- `<first_player>`: Who plays first, either `computer` or `human`.
- `[--depth <depth>]`: (Optional) Search depth for AI.

 Examples
Here are some example commands to run the game:

1. Standard Game with Human First:
   python nim_game.py 5 7 standard human
   This command starts a standard game with 5 red marbles and 7 blue marbles, with the human playing first.

2. Misère Game with Computer First:
   python nim_game.py 3 4 misere computer
   This command starts a misère game with 3 red marbles and 4 blue marbles, with the computer playing first.

3. Standard Game with Computer First and AI Depth of 3:
   python nim_game.py 10 5 standard computer --depth 3
   This command starts a standard game with 10 red marbles and 5 blue marbles, with the computer playing first and an AI search depth of 3.

 Detailed Example
Let's break down a detailed example command:
python nim_game.py 6 8 misere human --depth 4

- `6`: Number of red marbles.
- `8`: Number of blue marbles.
- `misere`: Misère game version.
- `human`: Human plays first.
- `--depth 4`: Optional argument to set the AI search depth to 4.

 Running the Command
1. Open your terminal or command prompt.
2. Navigate to the directory where `nim_game.py` is located.
3. Enter one of the example commands above, or modify the arguments to fit your desired game setup.
4. Press Enter to run the game.

This will start the game based on your specified parameters, and you can interact with it according to the rules defined in the script.