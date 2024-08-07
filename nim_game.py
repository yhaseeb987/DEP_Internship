import argparse
import random

class NimGame:
    def __init__(self, num_red, num_blue, version, first_player, depth=5):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth

    def is_game_over(self):
        return self.num_red == 0 or self.num_blue == 0

    def get_score(self):
        return self.num_red * 2 + self.num_blue * 3

    def print_state(self):
        print(f"Red marbles: {self.num_red}, Blue marbles: {self.num_blue}")

    def human_move(self):
        while True:
            try:
                red = int(input("Enter number of red marbles to pick: "))
                blue = int(input("Enter number of blue marbles to pick: "))
                if 0 <= red <= self.num_red and 0 <= blue <= self.num_blue and (red > 0 or blue > 0):
                    self.num_red -= red
                    self.num_blue -= blue
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

    def computer_move(self):
        _, move = self.minmax(self.num_red, self.num_blue, self.depth, True, float('-inf'), float('inf'))
        self.num_red -= move[0]
        self.num_blue -= move[1]
        print(f"Computer picked {move[0]} red marbles and {move[1]} blue marbles.")

    def minmax(self, red, blue, depth, is_maximizing, alpha, beta):
        if self.is_game_over() or depth == 0:
            return (self.evaluate_state(red, blue), None)

        moves = self.get_possible_moves(red, blue)
        if is_maximizing:
            max_eval = float('-inf')
            best_move = None
            for move in moves:
                new_red = red - move[0]
                new_blue = blue - move[1]
                eval, _ = self.minmax(new_red, new_blue, depth - 1, False, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return (max_eval, best_move)
        else:
            min_eval = float('inf')
            best_move = None
            for move in moves:
                new_red = red - move[0]
                new_blue = blue - move[1]
                eval, _ = self.minmax(new_red, new_blue, depth - 1, True, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return (min_eval, best_move)

    def get_possible_moves(self, red, blue):
        moves = []
        for i in range(1, 3):
            if red >= i:
                moves.append((i, 0))
            if blue >= i:
                moves.append((0, i))
        if self.version == 'standard':
            random.shuffle(moves)
        else:
            moves = moves[::-1]
        return moves

    def evaluate_state(self, red, blue):
        if self.is_game_over():
            if self.version == 'standard':
                return float('-inf') if self.current_player == 'computer' else float('inf')
            else:
                return float('inf') if self.current_player == 'computer' else float('-inf')
        return self.get_score()

    def play_game(self):
        self.print_state()
        while not self.is_game_over():
            if self.current_player == 'human':
                self.human_move()
                self.current_player = 'computer'
            else:
                self.computer_move()
                self.current_player = 'human'
            self.print_state()
        print("Game over!")
        print(f"Final score: {self.get_score()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Red-Blue Nim Game")
    parser.add_argument("num_red", type=int, help="Number of red marbles")
    parser.add_argument("num_blue", type=int, help="Number of blue marbles")
    parser.add_argument("version", choices=["standard", "misere"], default="standard", help="Game version")
    parser.add_argument("first_player", choices=["computer", "human"], default="computer", help="First player")
    parser.add_argument("--depth", type=int, help="Search depth for AI (optional)", default=5)
    args = parser.parse_args()

    game = NimGame(args.num_red, args.num_blue, args.version, args.first_player, args.depth)
    game.play_game()
